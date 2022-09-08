import json
import re

from app.base.logger import logger
from fastapi.encoders import jsonable_encoder
from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp, Message

routes_without_middleware = ["/download/*"]


class DebugApiMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def set_body(self, request: Request) -> None:
        receive_ = await request._receive()

        async def receive() -> Message:
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        isExcludeRouter = False

        for path in routes_without_middleware:
            x = re.search(path, request.url.path)
            if x is not None:
                isExcludeRouter = True

        if isExcludeRouter:
            return await call_next(request)
        else:
            await self.set_body(request)
            body = await request.body()
            response = await call_next(request)
            response_body = [chunk async for chunk in response.body_iterator]  # type: ignore
            response.body_iterator = iterate_in_threadpool(iter(response_body))  # type: ignore
            content = (b"".join(response_body)).decode()

            message = {
                "req": {
                    "api": request.url.path,
                    "method": request.method,
                    "query_string": request.query_params.__str__(),
                    "body": str(body),
                },
                "resp": content,
            }
            logger.debug(jsonable_encoder(message))
            return response
