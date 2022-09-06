from enum import Enum
from typing import Union

from pydantic import BaseModel


class Level(str, Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"


class ReqDemoWriteLog(BaseModel):
    level: Union[Level, None] = None
    message: str
