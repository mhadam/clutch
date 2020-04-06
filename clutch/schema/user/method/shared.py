from typing import Union, Sequence

from clutch.compat import Literal

IdsArg = Union[int, Sequence[Union[int, str]], Literal["recently_active"]]
