from enum import Enum, unique


@unique
class IpProtocol(Enum):
    IPV6 = "ipv6"
    IPV4 = "ipv4"
