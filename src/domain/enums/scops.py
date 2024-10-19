from enum import Enum


class ScopeUser(str, Enum):
    READ = "USER:READ"
    WRITE = "USER:WRITE"
    UPDATE = "USER:UPDATE"
    DELETE = "USER:DELETE"
