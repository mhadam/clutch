from typing import Mapping

from clutch.method.convert.argument.shared import convert_arguments
from clutch.method.typing.session.accessor import SessionAccessorArguments
from clutch.method.typing.session.mutator import SessionMutatorArguments
from clutch.method.typing.session.shared import Units


def _convert_units(units: Units) -> Mapping[str, object]:
    return convert_arguments(units, default_hyphenate=True)


def convert_mutator(arguments: SessionMutatorArguments) -> Mapping[str, object]:
    return convert_arguments(
        arguments,
        {"units": _convert_units},
        camelcase=frozenset({"seed_ratio_limited", "seed_ratio_limit"}),
        default_hyphenate=True,
    )


def convert_accessor(arguments: SessionAccessorArguments) -> Mapping[str, object]:
    return convert_arguments(
        arguments,
        {"units": _convert_units},
        camelcase=frozenset({"seed_ratio_limited", "seed_ratio_limit"}),
        default_hyphenate=True,
    )
