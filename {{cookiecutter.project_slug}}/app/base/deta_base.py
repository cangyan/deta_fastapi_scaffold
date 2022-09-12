from app.base.config import getProjectKey, settings
from deta import Deta

deta = Deta(getProjectKey())

db = deta.Base(settings.PROJECT_NAME)
