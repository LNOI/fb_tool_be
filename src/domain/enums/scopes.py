from enum import Enum


class ScopeUser(str, Enum):
    ALL = "user:all"


class ScopePlan(str, Enum):
    TRIAL = "plan:trial"
    BASIC = "plan:basic"
    PRO = "plan:pro"


class ScopeGroup(str, Enum):
    ALL = "group:all"


class ScopeHistoryScrape(str, Enum):
    ALL = "hc:all"


class ScopePost(str, Enum):
    ALL = "post:all"


class ScopeComment(str, Enum):
    ALL = "comment:all"


class ScopeMessage(str, Enum):
    ALL = "message:all"
