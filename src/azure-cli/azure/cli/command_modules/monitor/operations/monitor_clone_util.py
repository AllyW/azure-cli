# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.transform import _parse_id
from msrestazure.tools import parse_resource_id
from knack.log import get_logger
from knack.util import CLIError

from .._client_factory import cf_monitor
from ..util import gen_guid

logger = get_logger(__name__)
CLONED_NAME = "cloned-{}-{}"


def _gen_metrics_alert_rules_clone_list(monitor_client, source_resource, target_resource):
    alert_rules = list(monitor_client.metric_alerts.list_by_subscription())
    for alert_rule in alert_rules:
        if source_resource in alert_rule.scopes:
            if target_resource not in alert_rule.scopes:
                yield alert_rule
            else:
                logger.warning('The target resource already has alert rule %s. '
                               'Skip cloning this one.', alert_rule.name)


def _get_metrics_alert_rules_clone_list(cmd, source_resource, target_resource):
    subscription_id = parse_resource_id(source_resource)['subscription']
    from ..aaz.latest.monitor.metrics.alert import List
    alert_rules = List(cli_ctx=cmd.cli_ctx)(command_args={"subscription_id": subscription_id})
    for alert_rule in alert_rules:
        if source_resource in alert_rule['scopes']:
            if target_resource not in alert_rule.scopes:
                yield alert_rule
            else:
                logger.warning('The target resource already has alert rule %s. '
                               'Skip cloning this one.', alert_rule['name'])


def _add_into_existing_scopes(monitor_client, alert_rule, target_resource):
    alert_rule.scopes.append(target_resource)
    resource_group_name, name = _parse_id(alert_rule.id).values()  # pylint: disable=unbalanced-dict-unpacking
    return monitor_client.metric_alerts.create_or_update(resource_group_name=resource_group_name,
                                                         rule_name=name,
                                                         parameters=alert_rule)


def _add_into_existing_scopes_v2(cmd, source_resource, alert_rule, target_resource):
    subscription_id = parse_resource_id(source_resource)['subscription']
    alert_rule['scopes'].append(target_resource)
    resource_group_name, name = _parse_id(alert_rule['id']).values()
    alert_rule["subscription_id"] = subscription_id
    alert_rule["resource_group"] = resource_group_name
    alert_rule["name"] = name
    from ..aaz.latest.monitor.metrics.alert import Update
    return Update(cli_ctx=cmd.cli_ctx)(command_args=alert_rule)


def _clone_and_replace_action_group(source_monitor_client, target_monitor_client,
                                    cmd, alert_rule, action_group_mapping, target_resource):
    for index, action in enumerate(alert_rule.actions):
        if action.action_group_id in action_group_mapping:
            alert_rule.actions[index] = action_group_mapping[action.action_group_id][1]
        else:
            resource_group_name, name = _parse_id(action.action_group_id).values()  # pylint: disable=unbalanced-dict-unpacking
            action_group = source_monitor_client.action_groups.get(resource_group_name, name)
            name = CLONED_NAME.format(name, gen_guid())
            resource_group_name, _ = _parse_id(target_resource).values()  # pylint: disable=unbalanced-dict-unpacking
            new_action_group = target_monitor_client.action_groups.create_or_update(resource_group_name,
                                                                                    name,
                                                                                    action_group)
            MetricAlertAction = cmd.get_models('MetricAlertAction', operation_group='metric_alerts')
            new_action = MetricAlertAction(action_group_id=new_action_group.id,
                                           web_hook_properties=action.web_hook_properties)
            alert_rule.actions[index] = new_action
            action_group_mapping[action.action_group_id] = [new_action_group.id, new_action]
    return alert_rule


def _clone_and_replace_action_group_v2(cmd, source_resource, alert_rule, action_group_mapping, target_resource):
    source_subscription_id = parse_resource_id(source_resource)['subscription']
    target_subscription_id = parse_resource_id(target_resource)['subscription']
    for index, action in enumerate(alert_rule['actions']):
        if action['actionGroupId'] in action_group_mapping:
            alert_rule['actions'][index] = action_group_mapping[action['actionGroupId']][1]
        else:
            resource_group_name, name = _parse_id(action["actionGroupId"]).values()  # pylint: disable=unbalanced-dict-unpacking
            from ..aaz.latest.monitor.action_group import Show
            action_group = Show(cli_ctx=cmd.cli_ctx)(command_args={
                'subscription_id': source_subscription_id,
                "resource_group": resource_group_name,
                "action_group_name": name,
            })

            from .action_groups import ActionGroupCreate
            name = CLONED_NAME.format(name, gen_guid())
            resource_group_name, _ = _parse_id(target_resource).values()  # pylint: disable=unbalanced-dict-unpacking
            action_group["subscription_id"] = target_subscription_id
            action_group["resource_group"] = resource_group_name
            action_group["action_group_name"] = name
            new_action_group = ActionGroupCreate(cli_ctx=cmd.cli_ctx)(command_args=action_group)
            new_action = {
                "action_group_id": new_action_group["id"],
                "web_hook_properties": action_group["web_hook_properties"]
            }
            alert_rule['actions'][index] = new_action
            action_group_mapping[action['actionGroupId']] = [new_action_group['id'], new_action]
    return alert_rule


def _clone_alert_rule(monitor_client, alert_rule, target_resource):
    alert_rule.scopes = [target_resource]
    resource_group_name, name = _parse_id(target_resource).values()  # pylint: disable=unbalanced-dict-unpacking
    name = CLONED_NAME.format(name, gen_guid())
    return monitor_client.metric_alerts.create_or_update(resource_group_name=resource_group_name,
                                                         rule_name=name,
                                                         parameters=alert_rule)


def _clone_alert_rule_v2(cmd, source_resource, alert_rule, target_resource):
    alert_rule['scopes'] = [target_resource]
    resource_group_name, name = _parse_id(target_resource).values()  # pylint: disable=unbalanced-dict-unpacking
    name = CLONED_NAME.format(name, gen_guid())
    subscription_id = parse_resource_id(source_resource)['subscription']
    alert_rule["subscription_id"] = subscription_id
    alert_rule["resource_group"] = resource_group_name
    alert_rule["name"] = name
    alert_rule["evaluation_frequency"] = alert_rule['evaluationFrequency']
    alert_rule["window_size"] = alert_rule['windowSize']
    alert_rule["criteria"] = alert_rule['criteria']
    alert_rule["target_resource_type"] = alert_rule['type']
    alert_rule["target_resource_region"] = alert_rule['targetResourceRegion']
    alert_rule["actions"] = alert_rule['actions']
    from ..aaz.latest.monitor.metrics.alert import Create
    return Create(cli_ctx=cmd.cli_ctx)(command_args=alert_rule)


def _clone_monitor_metrics_alerts(cmd, source_resource, target_resource, always_clone=False):
    same_rp, same_sub = _is_resource_type_same_and_sub_same(source_resource, target_resource)
    if not same_rp:
        raise CLIError('The target resource should be the same type with the source resource')
    # source_monitor_client = cf_monitor(cmd.cli_ctx, subscription_id=parse_resource_id(source_resource)['subscription'])
    # target_monitor_client = cf_monitor(cmd.cli_ctx, subscription_id=parse_resource_id(target_resource)['subscription'])
    updated_metrics_alert_rules = []
    action_group_mapping = {}
    from azure.core.exceptions import HttpResponseError
    for alert_rule in _get_metrics_alert_rules_clone_list(cmd, source_resource, target_resource):
        if always_clone or not same_sub:
            alert_rule = _clone_and_replace_action_group_v2(cmd, source_resource, alert_rule, action_group_mapping,
                                                            target_resource)
            alert_rule = _clone_alert_rule_v2(cmd, source_resource, alert_rule, target_resource)
        else:
            try:
                alert_rule = _add_into_existing_scopes_v2(cmd, source_resource, alert_rule, target_resource)
            except HttpResponseError as ex:  # Create new alert rule
                if ex.status_code == 400:
                    alert_rule = _clone_alert_rule_v2(cmd, source_resource, alert_rule, target_resource)
                else:
                    raise ex
        updated_metrics_alert_rules.append(alert_rule)

    return updated_metrics_alert_rules


def _is_resource_type_same_and_sub_same(source_resource, target_resource):
    source_dict = parse_resource_id(source_resource.lower())
    target_dict = parse_resource_id(target_resource.lower())
    same_rp = source_dict['namespace'] == target_dict['namespace'] and source_dict['type'] == target_dict['type']
    same_sub = source_dict['subscription'] == target_dict['subscription']
    return same_rp, same_sub
