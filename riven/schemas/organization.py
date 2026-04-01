from datetime import datetime
from typing import Optional

from pydantic import Field

from riven.helpers.datetime_helpers import get_utc_time
from riven.schemas.enums import PrimitiveType
from riven.schemas.riven_base import rivenBase
from riven.utils import create_random_username


class OrganizationBase(rivenBase):
    __id_prefix__ = PrimitiveType.ORGANIZATION.value


class Organization(OrganizationBase):
    id: str = OrganizationBase.generate_id_field()
    name: str = Field(create_random_username(), description="The name of the organization.", json_schema_extra={"default": "SincereYogurt"})
    created_at: Optional[datetime] = Field(default_factory=get_utc_time, description="The creation date of the organization.")
    privileged_tools: bool = Field(False, description="Whether the organization has access to privileged tools.")


class OrganizationCreate(OrganizationBase):
    name: Optional[str] = Field(None, description="The name of the organization.")
    privileged_tools: Optional[bool] = Field(False, description="Whether the organization has access to privileged tools.")


class OrganizationUpdate(OrganizationBase):
    name: Optional[str] = Field(None, description="The name of the organization.")
    privileged_tools: Optional[bool] = Field(False, description="Whether the organization has access to privileged tools.")
