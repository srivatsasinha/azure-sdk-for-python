# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DependencyLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DependencyLevel."""

    DIRECT = "Direct"
    DESCENDANT = "Descendant"


class DependencyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the dependency type."""

    REQUIRED_FOR_PREPARE = "RequiredForPrepare"
    REQUIRED_FOR_MOVE = "RequiredForMove"


class JobName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the job name."""

    INITIAL_SYNC = "InitialSync"


class MoveResourceInputType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the move resource input type."""

    MOVE_RESOURCE_ID = "MoveResourceId"
    MOVE_RESOURCE_SOURCE_ID = "MoveResourceSourceId"


class MoveState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the MoveResource states."""

    ASSIGNMENT_PENDING = "AssignmentPending"
    PREPARE_PENDING = "PreparePending"
    PREPARE_IN_PROGRESS = "PrepareInProgress"
    PREPARE_FAILED = "PrepareFailed"
    MOVE_PENDING = "MovePending"
    MOVE_IN_PROGRESS = "MoveInProgress"
    MOVE_FAILED = "MoveFailed"
    DISCARD_IN_PROGRESS = "DiscardInProgress"
    DISCARD_FAILED = "DiscardFailed"
    COMMIT_PENDING = "CommitPending"
    COMMIT_IN_PROGRESS = "CommitInProgress"
    COMMIT_FAILED = "CommitFailed"
    COMMITTED = "Committed"
    DELETE_SOURCE_PENDING = "DeleteSourcePending"
    RESOURCE_MOVE_COMPLETED = "ResourceMoveCompleted"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the provisioning states."""

    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
    CREATING = "Creating"
    FAILED = "Failed"


class ResolutionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the resolution type."""

    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the resource mover service."""

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class TargetAvailabilityZone(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the target availability zone."""

    ONE = "1"
    TWO = "2"
    THREE = "3"
    NA = "NA"


class ZoneRedundant(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the zone redundant resource setting."""

    ENABLE = "Enable"
    DISABLE = "Disable"
