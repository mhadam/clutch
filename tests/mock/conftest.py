import json
import logging
from pathlib import Path
from typing import Any, Callable

import pytest
import pytest_httpserver
from deepdiff import DeepDiff
from dirty_equals import FunctionCheck

from clutch.client import Client


@pytest.fixture(scope="function")
def client(httpserver):
    client = Client(port=httpserver.port)
    return client


def custom_compare(expect) -> Callable[[Any], bool]:
    def inner(actual):
        diff = DeepDiff(actual, expect, ignore_order=True)
        is_same = len(diff) == 0
        if not is_same:
            msg = json.dumps(
                {
                    "expect": expect,
                    "actual": actual,
                    "diff": json.loads(diff.to_json()),
                },
                indent=2,
            )
            logging.getLogger().warn(msg=msg)
        return is_same

    return inner


@pytest.fixture(scope="function")
def mocker(monkeypatch, httpserver):
    def set_mock(req=None, res=None):
        r = {k: v for k, v in res.items() if v is not None}
        if req is None:
            httpserver.expect_request(
                "/transmission/rpc", method="POST"
            ).respond_with_json(r)
        else:
            httpserver.expect_request(
                "/transmission/rpc",
                method="POST",
                json=FunctionCheck(custom_compare(req)),
            ).respond_with_json(r)

    return set_mock
