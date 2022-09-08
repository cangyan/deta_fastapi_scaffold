from app.base.config import settings
from deta import Deta

deta = Deta(settings.PROJECT_KEY)

db = deta.Base(settings.PROJECT_NAME)
