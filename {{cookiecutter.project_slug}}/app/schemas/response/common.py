from typing import Generic, TypeVar

from pydantic.generics import GenericModel

T = TypeVar("T")


class RestfulResponse(GenericModel, Generic[T]):
    code: int = 0
    msg: str = "成功"
    data: T
