# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Update(AAZCommand):
    """Update a Log Analytics workspace table.
    """

    _aaz_info = {
        "version": "2022-10-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/workspaces/{}/tables/{}", "2022-10-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

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
        _args_schema.table_name = AAZStrArg(
            options=["-n", "--name", "--table-name"],
            help="The name of the table.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name"],
            help="The name of the workspace.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
                max_length=63,
                min_length=4,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.plan = AAZStrArg(
            options=["--plan"],
            arg_group="Properties",
            help="Instruct the system how to handle and charge the logs ingested to this table.",
            enum={"Analytics": "Analytics", "Basic": "Basic"},
        )
        _args_schema.restore = AAZObjectArg(
            options=["--restore"],
            arg_group="Properties",
            help="Parameters of the restore operation that initiated this table.",
        )
        _args_schema.retention_time = AAZIntArg(
            options=["--retention-time"],
            arg_group="Properties",
            help="The table retention in days, between 4 and 730. Setting this property to -1 will default to the workspace retention.",
            fmt=AAZIntArgFormat(
                maximum=730,
                minimum=4,
            ),
        )
        _args_schema.schema = AAZObjectArg(
            options=["--schema"],
            arg_group="Properties",
            help="Table schema.",
        )
        _args_schema.search_job = AAZObjectArg(
            options=["--search-job"],
            arg_group="Properties",
            help="Parameters of the search job that initiated this table.",
        )
        _args_schema.total_retention_time = AAZIntArg(
            options=["--total-retention-time"],
            arg_group="Properties",
            help="The table total retention in days, between 4 and 2555. Setting this property to -1 will default to table retention.",
            fmt=AAZIntArgFormat(
                maximum=2555,
                minimum=4,
            ),
        )

        restore = cls._args_schema.restore
        restore.end_restore_time = AAZDateTimeArg(
            options=["end-restore-time"],
            help="The timestamp to end the restore by (UTC).",
        )
        restore.source_table = AAZStrArg(
            options=["source-table"],
            help="The table to restore data from.",
        )
        restore.start_restore_time = AAZDateTimeArg(
            options=["start-restore-time"],
            help="The timestamp to start the restore from (UTC).",
        )

        schema = cls._args_schema.schema
        schema.columns = AAZListArg(
            options=["columns"],
            help="A list of table custom columns.",
        )
        schema.description = AAZStrArg(
            options=["description"],
            help="Table description.",
        )
        schema.display_name = AAZStrArg(
            options=["display-name"],
            help="Table display name.",
        )
        schema.name = AAZStrArg(
            options=["name"],
            help="Table name.",
        )

        columns = cls._args_schema.schema.columns
        columns.Element = AAZObjectArg()

        _element = cls._args_schema.schema.columns.Element
        _element.data_type_hint = AAZStrArg(
            options=["data-type-hint"],
            help="Column data type logical hint.",
            enum={"armPath": "armPath", "guid": "guid", "ip": "ip", "uri": "uri"},
        )
        _element.description = AAZStrArg(
            options=["description"],
            help="Column description.",
        )
        _element.display_name = AAZStrArg(
            options=["display-name"],
            help="Column display name.",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="Column name.",
        )
        _element.type = AAZStrArg(
            options=["type"],
            help="Column data type.",
            enum={"boolean": "boolean", "dateTime": "dateTime", "dynamic": "dynamic", "guid": "guid", "int": "int", "long": "long", "real": "real", "string": "string"},
        )

        search_job = cls._args_schema.search_job
        search_job.description = AAZStrArg(
            options=["description"],
            help="Search job Description.",
        )
        search_job.end_search_time = AAZDateTimeArg(
            options=["end-search-time"],
            help="The timestamp to end the search by (UTC)",
        )
        search_job.limit = AAZIntArg(
            options=["limit"],
            help="Limit the search job to return up to specified number of rows.",
        )
        search_job.query = AAZStrArg(
            options=["query"],
            help="Search job query.",
        )
        search_job.start_search_time = AAZDateTimeArg(
            options=["start-search-time"],
            help="The timestamp to start the search from (UTC)",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.TablesUpdate(ctx=self.ctx)()
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

    class TablesUpdate(AAZHttpOperation):
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
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/tables/{tableName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

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
                    "tableName", self.ctx.args.table_name,
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
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("plan", AAZStrType, ".plan")
                properties.set_prop("restoredLogs", AAZObjectType, ".restore")
                properties.set_prop("retentionInDays", AAZIntType, ".retention_time")
                properties.set_prop("schema", AAZObjectType, ".schema")
                properties.set_prop("searchResults", AAZObjectType, ".search_job")
                properties.set_prop("totalRetentionInDays", AAZIntType, ".total_retention_time")

            restored_logs = _builder.get(".properties.restoredLogs")
            if restored_logs is not None:
                restored_logs.set_prop("endRestoreTime", AAZStrType, ".end_restore_time")
                restored_logs.set_prop("sourceTable", AAZStrType, ".source_table")
                restored_logs.set_prop("startRestoreTime", AAZStrType, ".start_restore_time")

            schema = _builder.get(".properties.schema")
            if schema is not None:
                schema.set_prop("columns", AAZListType, ".columns")
                schema.set_prop("description", AAZStrType, ".description")
                schema.set_prop("displayName", AAZStrType, ".display_name")
                schema.set_prop("name", AAZStrType, ".name")

            columns = _builder.get(".properties.schema.columns")
            if columns is not None:
                columns.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.schema.columns[]")
            if _elements is not None:
                _elements.set_prop("dataTypeHint", AAZStrType, ".data_type_hint")
                _elements.set_prop("description", AAZStrType, ".description")
                _elements.set_prop("displayName", AAZStrType, ".display_name")
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("type", AAZStrType, ".type")

            search_results = _builder.get(".properties.searchResults")
            if search_results is not None:
                search_results.set_prop("description", AAZStrType, ".description")
                search_results.set_prop("endSearchTime", AAZStrType, ".end_search_time")
                search_results.set_prop("limit", AAZIntType, ".limit")
                search_results.set_prop("query", AAZStrType, ".query")
                search_results.set_prop("startSearchTime", AAZStrType, ".start_search_time")

            return self.serialize_content(_content_value)

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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
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

            restored_logs = cls._schema_on_200.properties.restored_logs
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

            result_statistics = cls._schema_on_200.properties.result_statistics
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

            schema = cls._schema_on_200.properties.schema
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

            categories = cls._schema_on_200.properties.schema.categories
            categories.Element = AAZStrType()

            columns = cls._schema_on_200.properties.schema.columns
            columns.Element = AAZObjectType()
            _UpdateHelper._build_schema_column_read(columns.Element)

            labels = cls._schema_on_200.properties.schema.labels
            labels.Element = AAZStrType()

            solutions = cls._schema_on_200.properties.schema.solutions
            solutions.Element = AAZStrType()

            standard_columns = cls._schema_on_200.properties.schema.standard_columns
            standard_columns.Element = AAZObjectType()
            _UpdateHelper._build_schema_column_read(standard_columns.Element)

            search_results = cls._schema_on_200.properties.search_results
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

            system_data = cls._schema_on_200.system_data
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


class _UpdateHelper:
    """Helper class for Update"""

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


__all__ = ["Update"]
