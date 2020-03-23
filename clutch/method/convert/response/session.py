from typing import Mapping

from clutch.method.convert.response.shared import convert_response_arguments
from clutch.method.typing.session.accessor import SessionAccessorResponse
from clutch.method.typing.session.stats import SessionStatsResponse


def convert_accessor_response(
    arguments: Mapping[str, object]
) -> SessionAccessorResponse:
    return convert_response_arguments(
        arguments, processors={"units": convert_response_arguments,}
    )


def convert_stats(arguments: Mapping[str, object]) -> SessionStatsResponse:
    return convert_response_arguments(
        arguments,
        processors={
            "current_stats": convert_response_arguments,
            "cumulative_stats": convert_response_arguments,
        },
    )
