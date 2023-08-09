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
    "monitor activity-log list",
)
class List(AAZCommand):
    """List and query activity log events.

    :example: List all events from July 1st, looking forward one week.
        az monitor activity-log list --start-time 2018-07-01 --offset 7d

    :example: List events within the past six hours based on a correlation ID.
        az monitor activity-log list --correlation-id b5eac9d2-e829-4c9a-9efb-586d19417c5f

    :example: List events within the past hour based on resource group.
        az monitor activity-log list -g {ResourceGroup} --offset 1h
    """

    _aaz_info = {
        "version": "2015-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.insights/eventtypes/management/values", "2015-04-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="Reduces the set of data collected.<br>This argument is required and it also requires at least the start date/time.<br>The **$filter** argument is very restricted and allows only the following patterns.<br>- *List events for a resource group*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceGroupName eq 'resourceGroupName'.<br>- *List events for resource*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceUri eq 'resourceURI'.<br>- *List events for a subscription in a time range*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z'.<br>- *List events for a resource provider*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceProvider eq 'resourceProviderName'.<br>- *List events for a correlation Id*: $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and correlationId eq 'correlationID'.<br><br>**NOTE**: No other syntax is allowed.",
            required=True,
        )
        _args_schema.select = AAZStrArg(
            options=["--select"],
            help="Used to fetch events with only the given properties.<br>The **$select** argument is a comma separated list of property names to be returned. Possible values are: *authorization*, *claims*, *correlationId*, *description*, *eventDataId*, *eventName*, *eventTimestamp*, *httpRequest*, *level*, *operationId*, *operationName*, *properties*, *resourceGroupName*, *resourceProviderName*, *resourceId*, *status*, *submissionTimestamp*, *subStatus*, *subscriptionId*",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ActivityLogsList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ActivityLogsList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.Insights/eventtypes/management/values",
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
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                    required=True,
                ),
                **self.serialize_query_param(
                    "$select", self.ctx.args.select,
                ),
                **self.serialize_query_param(
                    "api-version", "2015-04-01",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.authorization = AAZObjectType()
            _element.caller = AAZStrType(
                flags={"read_only": True},
            )
            _element.category = AAZObjectType()
            _ListHelper._build_schema_localizable_string_read(_element.category)
            _element.claims = AAZDictType(
                flags={"read_only": True},
            )
            _element.correlation_id = AAZStrType(
                serialized_name="correlationId",
                flags={"read_only": True},
            )
            _element.description = AAZStrType(
                flags={"read_only": True},
            )
            _element.event_data_id = AAZStrType(
                serialized_name="eventDataId",
                flags={"read_only": True},
            )
            _element.event_name = AAZObjectType(
                serialized_name="eventName",
            )
            _ListHelper._build_schema_localizable_string_read(_element.event_name)
            _element.event_timestamp = AAZStrType(
                serialized_name="eventTimestamp",
                flags={"read_only": True},
            )
            _element.http_request = AAZObjectType(
                serialized_name="httpRequest",
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.level = AAZStrType(
                flags={"read_only": True},
            )
            _element.operation_id = AAZStrType(
                serialized_name="operationId",
                flags={"read_only": True},
            )
            _element.operation_name = AAZObjectType(
                serialized_name="operationName",
            )
            _ListHelper._build_schema_localizable_string_read(_element.operation_name)
            _element.properties = AAZDictType(
                flags={"read_only": True},
            )
            _element.resource_group_name = AAZStrType(
                serialized_name="resourceGroupName",
                flags={"read_only": True},
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"read_only": True},
            )
            _element.resource_provider_name = AAZObjectType(
                serialized_name="resourceProviderName",
            )
            _element.resource_type = AAZObjectType(
                serialized_name="resourceType",
            )
            _element.status = AAZObjectType()
            _ListHelper._build_schema_localizable_string_read(_element.status)
            _element.sub_status = AAZObjectType(
                serialized_name="subStatus",
            )
            _ListHelper._build_schema_localizable_string_read(_element.sub_status)
            _element.submission_timestamp = AAZStrType(
                serialized_name="submissionTimestamp",
                flags={"read_only": True},
            )
            _element.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"read_only": True},
            )
            _element.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )

            authorization = cls._schema_on_200.value.Element.authorization
            authorization.action = AAZStrType()
            authorization.role = AAZStrType()
            authorization.scope = AAZStrType()

            claims = cls._schema_on_200.value.Element.claims
            claims.Element = AAZStrType()

            http_request = cls._schema_on_200.value.Element.http_request
            http_request.client_ip_address = AAZStrType(
                serialized_name="clientIpAddress",
            )
            http_request.client_request_id = AAZStrType(
                serialized_name="clientRequestId",
            )
            http_request.method = AAZStrType()
            http_request.uri = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.Element = AAZStrType()

            resource_provider_name = cls._schema_on_200.value.Element.resource_provider_name
            resource_provider_name.localized_value = AAZStrType(
                serialized_name="localizedValue",
            )
            resource_provider_name.value = AAZStrType(
                flags={"required": True},
            )

            resource_type = cls._schema_on_200.value.Element.resource_type
            resource_type.localized_value = AAZStrType(
                serialized_name="localizedValue",
            )
            resource_type.value = AAZStrType(
                flags={"required": True},
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_localizable_string_read = None

    @classmethod
    def _build_schema_localizable_string_read(cls, _schema):
        if cls._schema_localizable_string_read is not None:
            _schema.localized_value = cls._schema_localizable_string_read.localized_value
            _schema.value = cls._schema_localizable_string_read.value
            return

        cls._schema_localizable_string_read = _schema_localizable_string_read = AAZObjectType()

        localizable_string_read = _schema_localizable_string_read
        localizable_string_read.localized_value = AAZStrType(
            serialized_name="localizedValue",
        )
        localizable_string_read.value = AAZStrType(
            flags={"required": True},
        )

        _schema.localized_value = cls._schema_localizable_string_read.localized_value
        _schema.value = cls._schema_localizable_string_read.value


__all__ = ["List"]
