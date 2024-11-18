from typing import Any

import pytest

from verzeichnisdienst.v1.models import ApiRecord, ContactInfo, ServiceInfo

from .example_jsons_v1 import api_record, contact_info, service_info


@pytest.mark.parametrize(
    "json_dict",
    [
        api_record,
    ],
)
def test_api_record(json_dict: dict[str, Any]) -> None:
    model = ApiRecord.model_validate(json_dict)
    re_serialized = model.model_dump(mode="json")
    assert re_serialized == json_dict


@pytest.mark.parametrize(
    "json_dict",
    [
        contact_info,
    ],
)
def test_contact_record(json_dict: dict[str, Any]) -> None:
    model = ContactInfo.model_validate(json_dict)
    re_serialized = model.model_dump(mode="json")
    assert re_serialized == json_dict


@pytest.mark.parametrize(
    "json_dict",
    [
        service_info,
    ],
)
def test_service_inf(json_dict: dict[str, Any]) -> None:
    model = ServiceInfo.model_validate(json_dict)
    re_serialized = model.model_dump(mode="json")
    assert re_serialized == json_dict
