def test_bandwidth_groups(httpserver, mocker, client):
    mocker(
        req={"method": "group-get", "arguments": {"group": "abc"}},
        res={
            "result": "success",
            "arguments": {
                "group": [
                    {
                        "honorsSessionLimits": True,
                        "name": "",
                        "speed-limit-down-enabled": True,
                        "speed-limit-down": 1,
                        "speed-limit-up-enabled": True,
                        "speed-limit-up": 1,
                    }
                ]
            },
        },
    )
    _ = client.misc.bandwidth_groups(group="abc")
    httpserver.check_assertions()
