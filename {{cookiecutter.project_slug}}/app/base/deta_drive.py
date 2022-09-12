from app.base.config import getProjectKey, settings
from deta import Deta

deta = Deta(getProjectKey())

drive = deta.Drive(settings.PROJECT_NAME)
