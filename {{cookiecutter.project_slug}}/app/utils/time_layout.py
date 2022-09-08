from datetime import datetime


def getCurrentTimeStr() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def getFilePrefix() -> str:
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S")
