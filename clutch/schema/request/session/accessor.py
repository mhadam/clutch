from typing import Literal

from pydantic import BaseModel, Field, field_validator

from clutch.network.rpc.convert import to_camel, to_hyphen

SessionAccessorRequestField = Literal[
    "alt-speed-down",
    "alt-speed-enabled",
    "alt-speed-time-begin",
    "alt-speed-time-day",
    "alt-speed-time-enabled",
    "alt-speed-time-end",
    "alt-speed-up",
    "blocklist-enabled",
    "blocklist-size",
    "blocklist-url",
    "cache-size-mb",
    "config-dir",
    "default-trackers",
    "dht-enabled",
    "download-dir",
    "download-queue-enabled",
    "download-queue-size",
    "encryption",
    "idle-seeding-limit-enabled",
    "idle-seeding-limit",
    "incomplete-dir-enabled",
    "incomplete-dir",
    "lpd-enabled",
    "peer-limit-global",
    "peer-limit-per-torrent",
    "peer-port-random-on-start",
    "peer-port",
    "pex-enabled",
    "port-forwarding-enabled",
    "queue-stalled-enabled",
    "queue-stalled-minutes",
    "rename-partial-files",
    "reqq",
    "rpc-version-minimum",
    "rpc-version-semver",
    "rpc-version",
    "script-torrent-added-enabled",
    "script-torrent-added-filename",
    "script-torrent-done-enabled",
    "script-torrent-done-filename",
    "script-torrent-done-seeding-enabled",
    "script-torrent-done-seeding-filename",
    "seed-queue-enabled",
    "seed-queue-size",
    "seedRatioLimit",
    "seedRatioLimited",
    "session-id",
    "speed-limit-down-enabled",
    "speed-limit-down",
    "speed-limit-up-enabled",
    "speed-limit-up",
    "start-added-torrents",
    "trash-original-torrent-files",
    "units",
    "utp-enabled",
    "version",
]


class SessionAccessorArgumentsRequest(BaseModel):
    accessor_fields: set[SessionAccessorRequestField] | None = Field(
        None, serialization_alias="fields"
    )

    @field_validator("accessor_fields", mode="before")
    @classmethod
    def accessor_fields_format(cls, v):
        if v is None:
            return v
        camel = ["seed_ratio_limit", "seed_ratio_limited"]
        result = set()
        try:
            for field in v:
                if field in camel:
                    result.add(to_camel(field))
                else:
                    result.add(to_hyphen(field))
        except TypeError:
            return v
        return result
