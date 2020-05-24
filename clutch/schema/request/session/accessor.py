from typing import Set, Optional

from pydantic import BaseModel, Field, validator

from clutch.compat import Literal
from clutch.network.rpc.convert import to_camel, to_hyphen

SessionAccessorRequestField = Literal[
    "alt-speed-down",
    "alt-speed-enabled",
    "alt-speed-time-begin",
    "alt-speed-time-enabled",
    "alt-speed-time-end",
    "alt-speed-time-day",
    "alt-speed-up",
    "blocklist-url",
    "blocklist-enabled",
    "blocklist-size",
    "cache-size-mb",
    "config-dir",
    "download-dir",
    "download-queue-size",
    "download-queue-enabled",
    "dht-enabled",
    "encryption",
    "idle-seeding-limit",
    "idle-seeding-limit-enabled",
    "incomplete-dir",
    "incomplete-dir-enabled",
    "lpd-enabled",
    "peer-limit-global",
    "peer-limit-per-torrent",
    "pex-enabled",
    "peer-port",
    "peer-port-random-on-start",
    "port-forwarding-enabled",
    "queue-stalled-enabled",
    "queue-stalled-minutes",
    "rename-partial-files",
    "rpc-version",
    "rpc-version-minimum",
    "script-torrent-done-filename",
    "script-torrent-done-enabled",
    "seedRatioLimit",
    "seedRatioLimited",
    "seed-queue-size",
    "seed-queue-enabled",
    "speed-limit-down",
    "speed-limit-down-enabled",
    "speed-limit-up",
    "speed-limit-up-enabled",
    "start-added-torrents",
    "trash-original-torrent-files",
    "units",
    "utp-enabled",
    "version",
]


class SessionAccessorArgumentsRequest(BaseModel):
    accessor_fields: Optional[Set[SessionAccessorRequestField]] = Field(
        None, alias="fields"
    )

    @validator("accessor_fields", pre=True)
    def accessor_fields_format(cls, v):
        if v is not None and isinstance(v, list):
            camel = ["seed_ratio_limit", "seed_ratio_limited"]
            result = []
            for field in v:
                if field in camel:
                    result.append(to_camel(field))
                else:
                    result.append(to_hyphen(field))
            return result
        else:
            return v
