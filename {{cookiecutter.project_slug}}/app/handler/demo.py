from pprint import pprint
from typing import Any

from app.event.demo import DemoEvents
from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event


@local_handler.register(event_name=DemoEvents.GET_CONFIG)  # type: ignore
def handle_demo_get_config(event: Event) -> Any:
    pprint(event)
