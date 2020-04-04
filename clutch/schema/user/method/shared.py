from typing import Union, Sequence
from clutch.compat import Literal

IdsArg = Union[int, Sequence[Union[str, int]], Literal["recently_active"]]
