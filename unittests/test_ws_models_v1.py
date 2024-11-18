from typing import Any

import pytest

from verzeichnisdienst.v1.websocket import ApiRecord

from .example_ws_jsons_v1 import api_record


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
