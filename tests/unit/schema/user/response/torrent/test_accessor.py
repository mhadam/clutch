from clutch.schema.user.response.torrent.accessor import TorrentAccessorObject


def test_optional_fields():
    data = {"error": "some string"}

    result = TorrentAccessorObject.construct(**data)

    # as of writing now, construct creates a model without any of the missing fields
    assert result.error == "some string"
