# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network watcher connection-monitor start",
)
class Start(AAZCommand):
    """Start the specified connection monitor.

    :example: Start the specified connection monitor.
        az network watcher connection-monitor start -l westus -n MyConnectionMonitorName
    """

    _aaz_info = {
        "version": "2022-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkwatchers/{}/connectionmonitors/{}/start", "2022-07-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.connection_monitor_name = AAZStrArg(
            options=["-n", "--name", "--connection-monitor-name"],
            help="Connection monitor name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.network_watcher_name = AAZStrArg(
            options=["--network-watcher-name"],
            help="The name of the Network Watcher resource.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group_name = AAZResourceGroupNameArg(
            options=["-g", "--resource-group-name"],
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ConnectionMonitorsStart(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class ConnectionMonitorsStart(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/start",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "connectionMonitorName", self.ctx.args.connection_monitor_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkWatcherName", self.ctx.args.network_watcher_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-07-01",
                    required=True,
                ),
            }
            return parameters

        def on_200(self, session):
            pass


class _StartHelper:
    """Helper class for Start"""


__all__ = ["Start"]
