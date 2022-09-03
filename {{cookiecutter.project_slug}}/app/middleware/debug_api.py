import json

from app.base.logger import logger
from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.base import (BaseHTTPMiddleware,
                                       RequestResponseEndpoint)
from starlette.requests import Request
from starlette.responses import Response


class DebugApiMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request:Request, call_next: RequestResponseEndpoint) -> Response:
        response = await call_next(request)
        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        content = (b''.join(response_body)).decode()

        body = await request.body()
        message = {
            "api": request.url.path,
            "method": request.method,
            "query_string": request.query_params.__str__(),
            "body": body.decode(),
            "resp": content
        }
        logger.debug(json.dumps(message))
        return response
