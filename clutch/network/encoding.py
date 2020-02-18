import json
from base64 import b64encode
from enum import Enum


class TransmissionJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value

        if isinstance(obj, set):
            return list(obj)
        # # date{,time} is represented as seconds since epoch
        # try:
        #     return int(time.mktime(o.timetuple()))
        # except [AttributeError, TypeError]:
        #     pass
        #
        # # time is represented as minutes since midnight
        # # (alt_speed_time_begin, alt_speed_time_end)
        # try:
        #     return o.minute + o.hour * 60
        # except AttributeError:
        #     pass
        #
        # # EnumItem or iterable of EnumItem can be collapsed with Enum.to_mask
        # try:
        #     if any(isinstance(i, EnumItem) for i in o):
        #         return Enum.to_mask(o)
        # except TypeError:
        #     pass
        #
        # # a byte stream is base64 encoded

        return json.JSONEncoder.default(self, obj)
