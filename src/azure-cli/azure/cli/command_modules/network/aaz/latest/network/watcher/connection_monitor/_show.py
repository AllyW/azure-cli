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
    "network watcher connection-monitor show",
)
class Show(AAZCommand):
    """Shows a connection monitor by name.

    :example: Show a connection monitor for the given name.
        az network watcher connection-monitor show -l westus -n MyConnectionMonitorName
    """

    _aaz_info = {
        "version": "2022-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkwatchers/{}/connectionmonitors/{}", "2022-07-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

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
        self.ConnectionMonitorsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ConnectionMonitorsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

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

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.auto_start = AAZBoolType(
                serialized_name="autoStart",
            )
            properties.connection_monitor_type = AAZStrType(
                serialized_name="connectionMonitorType",
                flags={"read_only": True},
            )
            properties.destination = AAZObjectType()
            properties.endpoints = AAZListType()
            properties.monitoring_interval_in_seconds = AAZIntType(
                serialized_name="monitoringIntervalInSeconds",
            )
            properties.monitoring_status = AAZStrType(
                serialized_name="monitoringStatus",
                flags={"read_only": True},
            )
            properties.notes = AAZStrType()
            properties.outputs = AAZListType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.source = AAZObjectType()
            properties.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"read_only": True},
            )
            properties.test_configurations = AAZListType(
                serialized_name="testConfigurations",
            )
            properties.test_groups = AAZListType(
                serialized_name="testGroups",
            )

            destination = cls._schema_on_200.properties.destination
            destination.address = AAZStrType()
            destination.port = AAZIntType()
            destination.resource_id = AAZStrType(
                serialized_name="resourceId",
            )

            endpoints = cls._schema_on_200.properties.endpoints
            endpoints.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.endpoints.Element
            _element.address = AAZStrType()
            _element.coverage_level = AAZStrType(
                serialized_name="coverageLevel",
            )
            _element.filter = AAZObjectType()
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
            )
            _element.scope = AAZObjectType()
            _element.type = AAZStrType()

            filter = cls._schema_on_200.properties.endpoints.Element.filter
            filter.items = AAZListType()
            filter.type = AAZStrType()

            items = cls._schema_on_200.properties.endpoints.Element.filter.items
            items.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.endpoints.Element.filter.items.Element
            _element.address = AAZStrType()
            _element.type = AAZStrType()

            scope = cls._schema_on_200.properties.endpoints.Element.scope
            scope.exclude = AAZListType()
            scope.include = AAZListType()

            exclude = cls._schema_on_200.properties.endpoints.Element.scope.exclude
            exclude.Element = AAZObjectType()
            _ShowHelper._build_schema_connection_monitor_endpoint_scope_item_read(exclude.Element)

            include = cls._schema_on_200.properties.endpoints.Element.scope.include
            include.Element = AAZObjectType()
            _ShowHelper._build_schema_connection_monitor_endpoint_scope_item_read(include.Element)

            outputs = cls._schema_on_200.properties.outputs
            outputs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.outputs.Element
            _element.type = AAZStrType()
            _element.workspace_settings = AAZObjectType(
                serialized_name="workspaceSettings",
            )

            workspace_settings = cls._schema_on_200.properties.outputs.Element.workspace_settings
            workspace_settings.workspace_resource_id = AAZStrType(
                serialized_name="workspaceResourceId",
            )

            source = cls._schema_on_200.properties.source
            source.port = AAZIntType()
            source.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"required": True},
            )

            test_configurations = cls._schema_on_200.properties.test_configurations
            test_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.test_configurations.Element
            _element.http_configuration = AAZObjectType(
                serialized_name="httpConfiguration",
            )
            _element.icmp_configuration = AAZObjectType(
                serialized_name="icmpConfiguration",
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.preferred_ip_version = AAZStrType(
                serialized_name="preferredIPVersion",
            )
            _element.protocol = AAZStrType(
                flags={"required": True},
            )
            _element.success_threshold = AAZObjectType(
                serialized_name="successThreshold",
            )
            _element.tcp_configuration = AAZObjectType(
                serialized_name="tcpConfiguration",
            )
            _element.test_frequency_sec = AAZIntType(
                serialized_name="testFrequencySec",
            )

            http_configuration = cls._schema_on_200.properties.test_configurations.Element.http_configuration
            http_configuration.method = AAZStrType()
            http_configuration.path = AAZStrType()
            http_configuration.port = AAZIntType()
            http_configuration.prefer_https = AAZBoolType(
                serialized_name="preferHTTPS",
            )
            http_configuration.request_headers = AAZListType(
                serialized_name="requestHeaders",
            )
            http_configuration.valid_status_code_ranges = AAZListType(
                serialized_name="validStatusCodeRanges",
            )

            request_headers = cls._schema_on_200.properties.test_configurations.Element.http_configuration.request_headers
            request_headers.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.test_configurations.Element.http_configuration.request_headers.Element
            _element.name = AAZStrType()
            _element.value = AAZStrType()

            valid_status_code_ranges = cls._schema_on_200.properties.test_configurations.Element.http_configuration.valid_status_code_ranges
            valid_status_code_ranges.Element = AAZStrType()

            icmp_configuration = cls._schema_on_200.properties.test_configurations.Element.icmp_configuration
            icmp_configuration.disable_trace_route = AAZBoolType(
                serialized_name="disableTraceRoute",
            )

            success_threshold = cls._schema_on_200.properties.test_configurations.Element.success_threshold
            success_threshold.checks_failed_percent = AAZIntType(
                serialized_name="checksFailedPercent",
            )
            success_threshold.round_trip_time_ms = AAZFloatType(
                serialized_name="roundTripTimeMs",
            )

            tcp_configuration = cls._schema_on_200.properties.test_configurations.Element.tcp_configuration
            tcp_configuration.destination_port_behavior = AAZStrType(
                serialized_name="destinationPortBehavior",
            )
            tcp_configuration.disable_trace_route = AAZBoolType(
                serialized_name="disableTraceRoute",
            )
            tcp_configuration.port = AAZIntType()

            test_groups = cls._schema_on_200.properties.test_groups
            test_groups.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.test_groups.Element
            _element.destinations = AAZListType(
                flags={"required": True},
            )
            _element.disable = AAZBoolType()
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.sources = AAZListType(
                flags={"required": True},
            )
            _element.test_configurations = AAZListType(
                serialized_name="testConfigurations",
                flags={"required": True},
            )

            destinations = cls._schema_on_200.properties.test_groups.Element.destinations
            destinations.Element = AAZStrType()

            sources = cls._schema_on_200.properties.test_groups.Element.sources
            sources.Element = AAZStrType()

            test_configurations = cls._schema_on_200.properties.test_groups.Element.test_configurations
            test_configurations.Element = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_connection_monitor_endpoint_scope_item_read = None

    @classmethod
    def _build_schema_connection_monitor_endpoint_scope_item_read(cls, _schema):
        if cls._schema_connection_monitor_endpoint_scope_item_read is not None:
            _schema.address = cls._schema_connection_monitor_endpoint_scope_item_read.address
            return

        cls._schema_connection_monitor_endpoint_scope_item_read = _schema_connection_monitor_endpoint_scope_item_read = AAZObjectType()

        connection_monitor_endpoint_scope_item_read = _schema_connection_monitor_endpoint_scope_item_read
        connection_monitor_endpoint_scope_item_read.address = AAZStrType()

        _schema.address = cls._schema_connection_monitor_endpoint_scope_item_read.address


__all__ = ["Show"]
