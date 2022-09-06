import json

from fastapi.encoders import jsonable_encoder
from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import Message

from app.base.logger import logger


class DebugApiMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive() -> Message:
            return receive_

        request._receive = receive

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        await self.set_body(request)
        body = await request.body()
        response = await call_next(request)
        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        content = (b"".join(response_body)).decode()

        message = {
            "req": {
                "api": request.url.path,
                "method": request.method,
                "query_string": request.query_params.__str__(),
                "body": body.decode(),
            },
            "resp": content,
        }
        logger.debug(jsonable_encoder(message))
        return response
