from pprint import pprint
from typing import Any

from app.event.demo import DemoEvents
from app.metric.demo import demoApiRequestCounter
from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event
from prometheus_fastapi_instrumentator import Instrumentator


@local_handler.register(event_name=DemoEvents.GET_CONFIG)
def handle_demo_get_config(event: Event) -> Any:
    pprint(event)
    demoApiRequestCounter.labels("test").inc()


