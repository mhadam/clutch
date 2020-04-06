from typing import Optional, Set

from pydantic import BaseModel, Field, validator

from clutch.compat import Literal
from clutch.network.rpc.convert import to_hyphen, to_camel
from clutch.schema.user.method.shared import IdsArg

AccessorFieldRequest = Literal[
    "activityDate",
    "addedDate",
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
    "files",
    "fileStats",
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
    "percentDone",
    "pieces",
    "pieceCount",
    "pieceSize",
    "priorities",
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
    "sizeWhenDone",
    "startDate",
    "status",
    "trackers",
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
    ids: Optional[IdsArg]
    format: Optional[Literal["objects", "table"]]
    accessor_fields: TorrentAccessorFieldsRequest = Field(
        ..., alias="fields"
    )  # this must be an alias for pydantic reasons

    @validator("accessor_fields", pre=True)
    def accessor_fields_format(cls, v):
        if v is not None and isinstance(v, list):
            hyphenated = ["peer_limit"]
            result = []
            for field in v:
                if field in hyphenated:
                    result.append(to_hyphen(field))
                else:
                    result.append(to_camel(field))
            return result
        else:
            return v
