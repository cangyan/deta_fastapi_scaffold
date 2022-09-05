from typing import Union

from pydantic import BaseModel


class ReqDemoWriteLog(BaseModel):
    level: Union[str, None] = None
    message: str
