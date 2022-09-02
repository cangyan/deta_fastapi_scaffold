import uuid
from datetime import datetime
from enum import Enum

from fastapi_events.registry.payload_schema import registry as payload_schema
from pydantic import BaseModel


class DemoEvents(Enum):
    GET_CONFIG = "DEMO_GET_CONFIG"


@payload_schema.register(event_name=DemoEvents.GET_CONFIG)
class GetConfigPayload(BaseModel):
    id: uuid.UUID
    created_at: datetime
