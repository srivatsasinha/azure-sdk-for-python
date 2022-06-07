# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AnomalyDetectorDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """detection direction."""

    BOTH = "Both"
    DOWN = "Down"
    UP = "Up"


class AnomalyIncidentStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """incident status

    only return for alerting incident result.
    """

    ACTIVE = "Active"
    RESOLVED = "Resolved"


class AnomalySeverity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """min alert severity."""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class AnomalyValue(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AnomalyValue."""

    AUTO_DETECT = "AutoDetect"
    ANOMALY = "Anomaly"
    NOT_ANOMALY = "NotAnomaly"


class ChangePointValue(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ChangePointValue."""

    AUTO_DETECT = "AutoDetect"
    CHANGE_POINT = "ChangePoint"
    NOT_CHANGE_POINT = "NotChangePoint"


class DataFeedAccessMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """data feed access mode, default is Private."""

    PRIVATE = "Private"
    PUBLIC = "Public"


class DataFeedAutoRollupMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """roll up method."""

    NONE = "None"
    SUM = "Sum"
    MAX = "Max"
    MIN = "Min"
    AVG = "Avg"
    COUNT = "Count"


class DataFeedGranularityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """granularity of the time series."""

    YEARLY = "Yearly"
    MONTHLY = "Monthly"
    WEEKLY = "Weekly"
    DAILY = "Daily"
    HOURLY = "Hourly"
    MINUTELY = "Minutely"
    CUSTOM = "Custom"


class DataFeedRollupType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """mark if the data feed need rollup."""

    NO_ROLLUP = "NoRollup"
    NEED_ROLLUP = "NeedRollup"
    ALREADY_ROLLUP = "AlreadyRollup"


class DataFeedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """data feed status."""

    ACTIVE = "Active"
    PAUSED = "Paused"


class DatasourceAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """authentication type for corresponding data source."""

    BASIC = "Basic"
    MANAGED_IDENTITY = "ManagedIdentity"
    AZURE_SQL_CONNECTION_STRING = "AzureSQLConnectionString"
    DATA_LAKE_GEN2_SHARED_KEY = "DataLakeGen2SharedKey"
    SERVICE_PRINCIPAL = "ServicePrincipal"
    SERVICE_PRINCIPAL_IN_KV = "ServicePrincipalInKV"


class DatasourceCredentialType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of data source credential."""

    AZURE_SQL_CONNECTION_STRING = "AzureSQLConnectionString"
    DATA_LAKE_GEN2_SHARED_KEY = "DataLakeGen2SharedKey"
    SERVICE_PRINCIPAL = "ServicePrincipal"
    SERVICE_PRINCIPAL_IN_KV = "ServicePrincipalInKV"


class DatasourceMissingDataPointFillType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """the type of fill missing point for anomaly detection."""

    SMART_FILLING = "SmartFilling"
    PREVIOUS_VALUE = "PreviousValue"
    CUSTOM_VALUE = "CustomValue"
    NO_FILLING = "NoFilling"


class DatasourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """data source type."""

    AZURE_APPLICATION_INSIGHTS = "AzureApplicationInsights"
    AZURE_BLOB = "AzureBlob"
    AZURE_COSMOS_DB = "AzureCosmosDB"
    AZURE_DATA_EXPLORER = "AzureDataExplorer"
    AZURE_DATA_LAKE_STORAGE_GEN2 = "AzureDataLakeStorageGen2"
    AZURE_EVENT_HUBS = "AzureEventHubs"
    AZURE_LOG_ANALYTICS = "AzureLogAnalytics"
    AZURE_TABLE = "AzureTable"
    INFLUX_DB = "InfluxDB"
    MONGO_DB = "MongoDB"
    MY_SQL = "MySql"
    POSTGRE_SQL = "PostgreSql"
    SQL_SERVER = "SqlServer"


class DetectionConditionOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """condition operator

    should be specified when combining multiple detection conditions.
    """

    AND = "AND"
    OR = "OR"


class FeedbackType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """feedback type."""

    ANOMALY = "Anomaly"
    CHANGE_POINT = "ChangePoint"
    PERIOD = "Period"
    COMMENT = "Comment"


class MetricAnomalyAlertConfigurationsOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """cross metrics operator

    should be specified when setting up multiple metric alerting configurations.
    """

    AND = "AND"
    OR = "OR"
    XOR = "XOR"


class MetricAnomalyAlertScopeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Anomaly scope."""

    ALL = "All"
    DIMENSION = "Dimension"
    TOP_N = "TopN"


class PeriodType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """the type of setting period."""

    AUTO_DETECT = "AutoDetect"
    ASSIGN_VALUE = "AssignValue"


class SnoozeScope(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """snooze scope."""

    METRIC = "Metric"
    SERIES = "Series"