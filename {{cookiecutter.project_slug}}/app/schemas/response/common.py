from typing import Generic, TypeVar

from pydantic.generics import GenericModel

T = TypeVar('T')

class RestfulResponse(GenericModel, Generic[T]):
	code: int
	msg: str
	data: T
