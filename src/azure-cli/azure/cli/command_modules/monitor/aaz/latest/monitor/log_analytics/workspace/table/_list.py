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
    "monitor log-analytics workspace table list",
)
class List(AAZCommand):
    """List all the tables for the given Log Analytics workspace.

    :example: List all the tables for the given Log Analytics workspace
        az monitor log-analytics workspace table list --resource-group MyResourceGroup --workspace-name MyWorkspace
    """

    _aaz_info = {
        "version": "2022-10-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/workspaces/{}/tables", "2022-10-01"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name"],
            help="The name of the workspace.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
                max_length=63,
                min_length=4,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.TablesListByWorkspace(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        return result

    class TablesListByWorkspace(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/tables",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-10-01",
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
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.archive_retention_in_days = AAZIntType(
                serialized_name="archiveRetentionInDays",
                flags={"read_only": True},
            )
            properties.last_plan_modified_date = AAZStrType(
                serialized_name="lastPlanModifiedDate",
                flags={"read_only": True},
            )
            properties.plan = AAZStrType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.restored_logs = AAZObjectType(
                serialized_name="restoredLogs",
            )
            properties.result_statistics = AAZObjectType(
                serialized_name="resultStatistics",
            )
            properties.retention_in_days = AAZIntType(
                serialized_name="retentionInDays",
            )
            properties.retention_in_days_as_default = AAZBoolType(
                serialized_name="retentionInDaysAsDefault",
                flags={"read_only": True},
            )
            properties.schema = AAZObjectType()
            properties.search_results = AAZObjectType(
                serialized_name="searchResults",
            )
            properties.total_retention_in_days = AAZIntType(
                serialized_name="totalRetentionInDays",
            )
            properties.total_retention_in_days_as_default = AAZBoolType(
                serialized_name="totalRetentionInDaysAsDefault",
                flags={"read_only": True},
            )

            restored_logs = cls._schema_on_200.value.Element.properties.restored_logs
            restored_logs.azure_async_operation_id = AAZStrType(
                serialized_name="azureAsyncOperationId",
                flags={"read_only": True},
            )
            restored_logs.end_restore_time = AAZStrType(
                serialized_name="endRestoreTime",
            )
            restored_logs.source_table = AAZStrType(
                serialized_name="sourceTable",
            )
            restored_logs.start_restore_time = AAZStrType(
                serialized_name="startRestoreTime",
            )

            result_statistics = cls._schema_on_200.value.Element.properties.result_statistics
            result_statistics.ingested_records = AAZIntType(
                serialized_name="ingestedRecords",
                flags={"read_only": True},
            )
            result_statistics.progress = AAZFloatType(
                flags={"read_only": True},
            )
            result_statistics.scanned_gb = AAZFloatType(
                serialized_name="scannedGb",
                flags={"read_only": True},
            )

            schema = cls._schema_on_200.value.Element.properties.schema
            schema.categories = AAZListType(
                flags={"read_only": True},
            )
            schema.columns = AAZListType()
            schema.description = AAZStrType()
            schema.display_name = AAZStrType(
                serialized_name="displayName",
            )
            schema.labels = AAZListType(
                flags={"read_only": True},
            )
            schema.name = AAZStrType()
            schema.solutions = AAZListType(
                flags={"read_only": True},
            )
            schema.source = AAZStrType(
                flags={"read_only": True},
            )
            schema.standard_columns = AAZListType(
                serialized_name="standardColumns",
                flags={"read_only": True},
            )
            schema.table_sub_type = AAZStrType(
                serialized_name="tableSubType",
                flags={"read_only": True},
            )
            schema.table_type = AAZStrType(
                serialized_name="tableType",
                flags={"read_only": True},
            )

            categories = cls._schema_on_200.value.Element.properties.schema.categories
            categories.Element = AAZStrType()

            columns = cls._schema_on_200.value.Element.properties.schema.columns
            columns.Element = AAZObjectType()
            _ListHelper._build_schema_column_read(columns.Element)

            labels = cls._schema_on_200.value.Element.properties.schema.labels
            labels.Element = AAZStrType()

            solutions = cls._schema_on_200.value.Element.properties.schema.solutions
            solutions.Element = AAZStrType()

            standard_columns = cls._schema_on_200.value.Element.properties.schema.standard_columns
            standard_columns.Element = AAZObjectType()
            _ListHelper._build_schema_column_read(standard_columns.Element)

            search_results = cls._schema_on_200.value.Element.properties.search_results
            search_results.azure_async_operation_id = AAZStrType(
                serialized_name="azureAsyncOperationId",
                flags={"read_only": True},
            )
            search_results.description = AAZStrType()
            search_results.end_search_time = AAZStrType(
                serialized_name="endSearchTime",
            )
            search_results.limit = AAZIntType()
            search_results.query = AAZStrType()
            search_results.source_table = AAZStrType(
                serialized_name="sourceTable",
                flags={"read_only": True},
            )
            search_results.start_search_time = AAZStrType(
                serialized_name="startSearchTime",
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_column_read = None

    @classmethod
    def _build_schema_column_read(cls, _schema):
        if cls._schema_column_read is not None:
            _schema.data_type_hint = cls._schema_column_read.data_type_hint
            _schema.description = cls._schema_column_read.description
            _schema.display_name = cls._schema_column_read.display_name
            _schema.is_default_display = cls._schema_column_read.is_default_display
            _schema.is_hidden = cls._schema_column_read.is_hidden
            _schema.name = cls._schema_column_read.name
            _schema.type = cls._schema_column_read.type
            return

        cls._schema_column_read = _schema_column_read = AAZObjectType()

        column_read = _schema_column_read
        column_read.data_type_hint = AAZStrType(
            serialized_name="dataTypeHint",
        )
        column_read.description = AAZStrType()
        column_read.display_name = AAZStrType(
            serialized_name="displayName",
        )
        column_read.is_default_display = AAZBoolType(
            serialized_name="isDefaultDisplay",
            flags={"read_only": True},
        )
        column_read.is_hidden = AAZBoolType(
            serialized_name="isHidden",
            flags={"read_only": True},
        )
        column_read.name = AAZStrType()
        column_read.type = AAZStrType()

        _schema.data_type_hint = cls._schema_column_read.data_type_hint
        _schema.description = cls._schema_column_read.description
        _schema.display_name = cls._schema_column_read.display_name
        _schema.is_default_display = cls._schema_column_read.is_default_display
        _schema.is_hidden = cls._schema_column_read.is_hidden
        _schema.name = cls._schema_column_read.name
        _schema.type = cls._schema_column_read.type


__all__ = ["List"]
