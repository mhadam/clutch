from typing import Literal, Set

from pydantic import BaseModel, Field, field_validator

from clutch.network.rpc.convert import to_camel, to_hyphen
from clutch.schema.user.method.shared import IdsArg

AccessorFieldRequest = Literal[
    "activityDate",
    "addedDate",
    "availability",
    "bandwidthPriority",
    "comment",
    "corruptEver",
    "creator",
    "dateCreated",
    "desiredAvailable",
    "doneDate",
    "downloadDir",
    "downloadedEver",
    "downloadLimit",
    "downloadLimited",
    "editDate",
    "error",
    "errorString",
    "eta",
    "etaIdle",
    "file-count",
    "files",
    "fileStats",
    "group",
    "hashString",
    "haveUnchecked",
    "haveValid",
    "honorsSessionLimits",
    "id",
    "isFinished",
    "isPrivate",
    "isStalled",
    "labels",
    "leftUntilDone",
    "magnetLink",
    "manualAnnounceTime",
    "maxConnectedPeers",
    "metadataPercentComplete",
    "name",
    "peer-limit",
    "peers",
    "peersConnected",
    "peersFrom",
    "peersGettingFromUs",
    "peersSendingToUs",
    "percentComplete",
    "percentDone",
    "pieces",
    "pieceCount",
    "pieceSize",
    "priorities",
    "primary-mime-type",
    "queuePosition",
    "rateDownload",
    "rateUpload",
    "recheckProgress",
    "secondsDownloading",
    "secondsSeeding",
    "seedIdleLimit",
    "seedIdleMode",
    "seedRatioLimit",
    "seedRatioMode",
    "sequentialDownload",
    "sizeWhenDone",
    "startDate",
    "status",
    "trackers",
    "trackerList",
    "trackerStats",
    "totalSize",
    "torrentFile",
    "uploadedEver",
    "uploadLimit",
    "uploadLimited",
    "uploadRatio",
    "wanted",
    "webseeds",
    "webseedsSendingToUs",
]

TorrentAccessorFieldsRequest = Set[AccessorFieldRequest]


class TorrentAccessorArgumentsRequest(BaseModel):
    ids: IdsArg | None = None
    format: Literal["objects", "table"] | None = None
    accessor_fields: TorrentAccessorFieldsRequest | None = Field(
        ..., serialization_alias="fields"
    )

    @field_validator("accessor_fields", mode="before")
    @classmethod
    def accessor_fields_format(cls, v):
        if v is not None:
            hyphenated = {"peer_limit"}
            result = set()
            try:
                for field in v:
                    if field in hyphenated:
                        result.add(to_hyphen(field))
                    else:
                        result.add(to_camel(field))
            except TypeError:
                return v
            return result
        else:
            return v
