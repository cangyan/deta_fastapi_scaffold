from app.base.config import settings
from deta import Deta

deta = Deta(settings.PROJECT_KEY)

drive = deta.Drive(settings.PROJECT_NAME)
