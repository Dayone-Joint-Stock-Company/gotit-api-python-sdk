# coding: utf-8

"""
    Sample API

    Technical document APIs for API Version 4.

    The version of the OpenAPI document: 4.0.0
    Contact: quang.huynh@gotit.vn
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class VOUCHERESCHEMA(BaseModel):
    """
    VOUCHERESCHEMA
    """ # noqa: E501
    voucher_link: Optional[StrictStr] = Field(default=None, description="Voucher of link e")
    voucher_cover_link: Optional[StrictStr] = Field(default=None, description="Voucher cover of link e")
    voucher_serial: Optional[StrictStr] = Field(default=None, description="Voucher serial of link e")
    value: Optional[StrictStr] = Field(default=None, description="Voucher value of link e")
    expired_date: Optional[StrictStr] = Field(default=None, description="Expiry date of voucher link Format: 'YYYY-MM-DD'")
    __properties: ClassVar[List[str]] = ["voucher_link", "voucher_cover_link", "voucher_serial", "value", "expired_date"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of VOUCHERESCHEMA from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if voucher_link (nullable) is None
        # and model_fields_set contains the field
        if self.voucher_link is None and "voucher_link" in self.model_fields_set:
            _dict['voucher_link'] = None

        # set to None if voucher_cover_link (nullable) is None
        # and model_fields_set contains the field
        if self.voucher_cover_link is None and "voucher_cover_link" in self.model_fields_set:
            _dict['voucher_cover_link'] = None

        # set to None if voucher_serial (nullable) is None
        # and model_fields_set contains the field
        if self.voucher_serial is None and "voucher_serial" in self.model_fields_set:
            _dict['voucher_serial'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if expired_date (nullable) is None
        # and model_fields_set contains the field
        if self.expired_date is None and "expired_date" in self.model_fields_set:
            _dict['expired_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VOUCHERESCHEMA from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "voucher_link": obj.get("voucher_link"),
            "voucher_cover_link": obj.get("voucher_cover_link"),
            "voucher_serial": obj.get("voucher_serial"),
            "value": obj.get("value"),
            "expired_date": obj.get("expired_date")
        })
        return _obj


