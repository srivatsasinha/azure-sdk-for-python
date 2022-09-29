# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
# pylint: disable=protected-access

## This is temprory class to work with custom applications programatically.
## This is a private preview work.

import re

from azure.ai.ml._restclient.v2022_10_01_preview.models import (
    CustomService,
    Docker,
    Endpoint,
    EnvironmentVariable,
    EnvironmentVariableType,
    Image,
    ImageType,
    Protocol,
    VolumeDefinition,
    VolumeDefinitionType,
)
from azure.ai.ml._utils._experimental import experimental
from azure.ai.ml.entities._mixins import RestTranslatableMixin
from azure.ai.ml.exceptions import ErrorCategory, ErrorTarget, ValidationException


@experimental
class CustomApplications(RestTranslatableMixin):

    APPLICATION_NAME = "applicationName"
    TARGET_PORT = "targetPort"
    PUBLISHED_PORT = "publishedPort"
    DOCKER_IMAGE = "dockerImage"
    ENV_VARS = "environmentVariables"
    BIND_MOUNTS = "bindMounts"
    SOURCE = "source"
    TARGET = "target"
    ENV_VAR_NAME = "name"
    ENV_VAR_VALUE = "value"
    TARGET_PORT_MIN_VALUE = 1
    TARGET_PORT_MAX_VALUE = 65535
    PUBLISHED_PORT_MIN_VALUE = 1025
    PUBLISHED_PORT_MAX_VALUE = 65535

    """Custom Application Resource
    param custom_app: Custom Application flat json passed by the user
    type custom_app: dict[str any]"""

    def __init__(self, custom_app: dict[str, any]):
        self.custom_app = custom_app
        self._validate_custom_app_input()

    def _to_rest_object(self):
        endpoints = [
            Endpoint(
                name="connect",
                target=self.custom_app[self.TARGET_PORT],
                published=self.custom_app[self.PUBLISHED_PORT],
                protocol=Protocol.HTTP,
            )
        ]
        docker_image = Image(type=ImageType.DOCKER, reference=self.custom_app[self.DOCKER_IMAGE])
        environment_variables = {}
        bind_mounts = []
        if self.ENV_VARS in self.custom_app.keys():
            for env_variable in self.custom_app[self.ENV_VARS]:
                environment_variables[env_variable[self.ENV_VAR_NAME]]: EnvironmentVariable(
                    type=EnvironmentVariableType.LOCAL, value=env_variable[self.ENV_VAR_VALUE]
                )
        if self.BIND_MOUNTS in self.custom_app.keys():
            for bind_mount in self.custom_app[self.BIND_MOUNTS]:
                bind_mounts.append(
                    VolumeDefinition(
                        type=VolumeDefinitionType.BIND,
                        read_only=False,
                        source=bind_mount[self.SOURCE],
                        target=bind_mount[self.TARGET],
                    )
                )
        return CustomService(
            docker=Docker(privileged=True),
            environment_variables=environment_variables,
            volumes=bind_mounts,
            endpoints=endpoints,
            image=docker_image,
            name=self.custom_app[self.APPLICATION_NAME],
        )

    def _validate_custom_app_input(self):
        missing_property_error_message = "{} is missing in one or more of the custom applications"
        invalid_value_error_message = "Value of {} property should be between {} and {}"

        if self.APPLICATION_NAME not in self.custom_app.keys():
            raise ValidationException(
                message=missing_property_error_message.format(self.APPLICATION_NAME),
                target=ErrorTarget.COMPUTE,
                no_personal_data_message=missing_property_error_message.format(self.APPLICATION_NAME),
                error_category=ErrorCategory.USER_ERROR,
            )
        if not re.compile(r"^([a-z0-9]([a-z0-9\-]{0,61}[a-z0-9])?)$").search(self.custom_app[self.APPLICATION_NAME]):
            raise ValidationException(
                message="One or more custom applications have invalid name.",
                target=ErrorTarget.COMPUTE,
                no_personal_data_message=missing_property_error_message.format(self.APPLICATION_NAME),
                error_category=ErrorCategory.USER_ERROR,
            )
        if self.TARGET_PORT not in self.custom_app.keys():
            raise ValidationException(
                message=missing_property_error_message.format(self.TARGET_PORT),
                target=ErrorTarget.COMPUTE,
                no_personal_data_message=missing_property_error_message.format(self.TARGET_PORT),
                error_category=ErrorCategory.USER_ERROR,
            )
        if not self.custom_app[self.TARGET_PORT].isdigit():
            msg = "Target port must be an integer"
            raise ValidationException(
                message=msg,
                target=ErrorTarget.COMPUTE,
                no_personal_data_message=msg,
                error_category=ErrorCategory.USER_ERROR,
            )
        targetPort = int(self.custom_app[self.TARGET_PORT])
        if not (targetPort >= self.TARGET_PORT_MIN_VALUE and targetPort <= self.TARGET_PORT_MAX_VALUE):
            raise ValidationException(
                message=invalid_value_error_message.format(
                    self.TARGET_PORT, self.TARGET_PORT_MIN_VALUE, self.TARGET_PORT_MAX_VALUE
                ),
                target=ErrorTarget.COMPUTE,
                no_personal_data_message=invalid_value_error_message.format(
                    self.TARGET_PORT, self.TARGET_PORT_MIN_VALUE, self.TARGET_PORT_MAX_VALUE
                ),
                error_category=ErrorCategory.USER_ERROR,
            )
        if self.PUBLISHED_PORT not in self.custom_app.keys():
            raise ValidationException(
                message=missing_property_error_message.format(self.TARGET_PORT),
                target=ErrorTarget.COMPUTE,
                no_personal_data_message=missing_property_error_message.format(self.TARGET_PORT),
                error_category=ErrorCategory.USER_ERROR,
            )
        if not self.custom_app[self.TARGET_PORT].isdigit():
            msg = "Published port must be an integer"
            raise ValidationException(
                message=msg,
                target=ErrorTarget.COMPUTE,
                no_personal_data_message=msg,
                error_category=ErrorCategory.USER_ERROR,
            )
        publishedPort = int(self.custom_app[self.TARGET_PORT])
        if not (publishedPort >= self.PUBLISHED_PORT_MIN_VALUE and publishedPort <= self.PUBLISHED_PORT_MAX_VALUE):
            raise ValidationException(
                message=invalid_value_error_message.format(
                    self.PUBLISHED_PORT, self.PUBLISHED_PORT_MIN_VALUE, self.PUBLISHED_PORT_MAX_VALUE
                ),
                target=ErrorTarget.COMPUTE,
                no_personal_data_message=invalid_value_error_message.format(
                    self.PUBLISHED_PORT, self.PUBLISHED_PORT_MIN_VALUE, self.PUBLISHED_PORT_MAX_VALUE
                ),
                error_category=ErrorCategory.USER_ERROR,
            )
        if self.DOCKER_IMAGE not in self.custom_app.keys():
            raise ValidationException(
                message=missing_property_error_message.format(self.DOCKER_IMAGE),
                target=ErrorTarget.COMPUTE,
                no_personal_data_message=missing_property_error_message.format(self.DOCKER_IMAGE),
                error_category=ErrorCategory.USER_ERROR,
            )

        missing_inner_property = "One or More {} is missing property {} in one or more custom applications"
        if self.BIND_MOUNTS in self.custom_app.keys():
            for bindMount in self.custom_app[self.BIND_MOUNTS]:
                if self.SOURCE not in bindMount.keys():
                    raise ValidationException(
                        message=missing_inner_property.format(self.BIND_MOUNTS, self.SOURCE),
                        target=ErrorTarget.COMPUTE,
                        no_personal_data_message=missing_inner_property.format(self.BIND_MOUNTS, self.SOURCE),
                        error_category=ErrorCategory.USER_ERROR,
                    )
                if self.TARGET not in bindMount.keys():
                    raise ValidationException(
                        message=missing_inner_property.format(self.BIND_MOUNTS, self.SOURCE),
                        target=ErrorTarget.COMPUTE,
                        no_personal_data_message=missing_inner_property.format(self.BIND_MOUNTS, self.SOURCE),
                        error_category=ErrorCategory.USER_ERROR,
                    )

        if self.ENV_VARS in self.custom_app.keys():
            for envVar in self.custom_app[self.ENV_VARS]:
                if self.ENV_VAR_NAME not in envVar.keys():
                    raise ValidationException(
                        message=missing_inner_property.format(self.ENV_VARS, self.ENV_VAR_NAME),
                        target=ErrorTarget.COMPUTE,
                        no_personal_data_message=missing_inner_property.format(self.ENV_VARS, self.ENV_VAR_NAME),
                        error_category=ErrorCategory.USER_ERROR,
                    )
                if self.ENV_VAR_VALUE not in envVar.keys():
                    raise ValidationException(
                        message=missing_inner_property.format(self.ENV_VARS, self.ENV_VAR_VALUE),
                        target=ErrorTarget.COMPUTE,
                        no_personal_data_message=missing_inner_property.format(self.ENV_VARS, self.ENV_VAR_VALUE),
                        error_category=ErrorCategory.USER_ERROR,
                    )

        return True

    @classmethod
    def _from_rest_object(cls, obj: CustomService) -> "dict[str,any]":
        if obj is None:
            return obj
        custom_app = {}
        custom_app[cls.APPLICATION_NAME] = obj.name
        custom_app[cls.TARGET_PORT] = obj.endpoints[0].target
        custom_app[cls.DOCKER_IMAGE] = obj.image.reference
        custom_app[cls.BIND_MOUNTS] = list(
            map(lambda bindMount: {cls.SOURCE: bindMount.source, cls.TARGET: bindMount.target}, obj.volumes)
        )
        custom_app[cls.ENV_VARS] = [
            {cls.ENV_VAR_NAME: varname, cls.ENV_VAR_VALUE: varvalue.value}
            for varname, varvalue in obj.environment_variables.items()
        ]
        return custom_app
