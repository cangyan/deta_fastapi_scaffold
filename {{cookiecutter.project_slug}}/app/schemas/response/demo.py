from pydantic import BaseModel


class Config(BaseModel):
    project_name: str


class WriteLog(BaseModel):
    result: str
    message: str
