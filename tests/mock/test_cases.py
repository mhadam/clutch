import logging
from typing import Callable, Any

from clutch.schema.user.method.torrent.action import TorrentActionMethod

from clutch import Client

test_cases: list[tuple[str, dict, dict, Callable[[Client], Any]]] = [
    (
        "torrent add",
        {
            "method": "torrent-add",
            "arguments": {"filename": "example.torrent"},
            "tag": 1,
        },
        {
            "result": "success",
            "arguments": {
                "torrent-added": {"id": 1, "name": "example", "hashString": "abc"}
            },
        },
        lambda c: c.torrent.add({"filename": "example.torrent"}, tag=1),
    ),
    (
        "torrent add with magnet link",
        {
            "method": "torrent-add",
            "arguments": {"filename": "magnet:?xt=urn:btih:examplehash"},
        },
        {
            "result": "success",
            "arguments": {
                "torrent-added": {
                    "id": 2,
                    "name": "magnet-example",
                    "hashString": "abc",
                }
            },
        },
        lambda c: c.torrent.add({"filename": "magnet:?xt=urn:btih:examplehash"}),
    ),
    (
        "torrent get with objects format",
        {
            "method": "torrent-get",
            "arguments": {"format": "objects", "fields": ["status", "name", "id"]},
            "tag": 2,
        },
        {
            "result": "success",
            "arguments": {
                "torrents": [
                    {"id": 1, "name": "example", "status": "downloading"},
                    {"id": 2, "name": "magnet-example", "status": "stopped"},
                ]
            },
        },
        lambda c: c.torrent.accessor(fields={"id", "name", "status"}, tag=2),
    ),
    (
        "torrent set location",
        {
            "method": "torrent-set-location",
            "arguments": {"ids": [1], "location": "/new/path", "move": True},
            "tag": 3,
        },
        {"result": "success"},
        lambda c: c.torrent.move([1], "/new/path", move=True, tag=3),
    ),
    (
        "torrent action - stop",
        {"method": "torrent-stop", "arguments": {"ids": [1]}},
        {"result": "success"},
        lambda c: c.torrent.action(TorrentActionMethod.STOP, ids=[1]),
    ),
    (
        "torrent start",
        {"method": "torrent-start", "arguments": {"ids": [2]}},
        {"result": "success"},
        lambda c: c.torrent.action(TorrentActionMethod.START, ids=[2]),
    ),
    (
        "torrent remove",
        {
            "method": "torrent-remove",
            "arguments": {"ids": [1], "delete-local-data": True},
            "tag": 4,
        },
        {"result": "success"},
        lambda c: c.torrent.remove(tag=4, delete_local_data=True, ids=[1]),
    ),
    (
        "session stats",
        {"method": "session-stats", "tag": 1},
        {
            "result": "success",
            "arguments": {
                "activeTorrentCount": 1,
                "downloadSpeed": 1024,
                "uploadSpeed": 512,
            },
        },
        lambda c: c.session.stats(tag=1),
    ),
    (
        "session set",
        {
            "method": "session-set",
            "arguments": {"download-dir": "/new/download/path"},
            "tag": 5,
        },
        {"result": "success"},
        lambda c: c.session.mutator(
            arguments={"download_dir": "/new/download/path"}, tag=5
        ),
    ),
    (
        "session get",
        {
            "method": "session-get",
            "arguments": {"fields": ["version", "rpc-version", "download-dir"]},
        },
        {
            "result": "success",
            "arguments": {
                "version": "3.00",
                "rpc-version": 17,
                "download-dir": "/new/download/path",
            },
        },
        lambda c: c.session.accessor(fields={"version", "rpc_version", "download_dir"}),
    ),
    (
        "free space",
        {"method": "free-space", "arguments": {"path": "/test/dir"}, "tag": 5},
        {
            "result": "success",
            "arguments": {
                "path": "/test/dir",
                "size-bytes": 1024 * 1024 * 1024,
            },
        },
        lambda c: c.misc.free_space(path="/test/dir", tag=5),
    ),
]


def test_all(client, httpserver, mocker):
    for i, case in enumerate(test_cases):
        desc, req, res, call = case
        logging.getLogger().info(f"running {desc}")
        mocker(req=req, res=res)
        try:
            call(client)
        except Exception as e:
            logging.getLogger().info(e)
        httpserver.check_assertions()
        httpserver.clear()
