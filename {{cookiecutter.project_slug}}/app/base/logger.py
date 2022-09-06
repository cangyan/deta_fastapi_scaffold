import json
import logging
from datetime import datetime

from app.base.config import settings


class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    # format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    format_str = "{message}"

    FORMATS = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: grey + format_str + reset,
        logging.WARNING: yellow + format_str + reset,
        logging.ERROR: red + format_str + reset,
        logging.CRITICAL: bold_red + format_str + reset,
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        # formatter = logging.Formatter()
        m = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "message": record.getMessage(),
            "filename": record.filename,
            "lineno": record.lineno,
        }
        return log_fmt.format(message=json.dumps(m, ensure_ascii=False))


logger = logging.getLogger(__name__)
level = logging.getLevelName(settings.LOG_LEVEL.upper())
logger.setLevel(level)

ch = logging.StreamHandler()
fh = logging.FileHandler(filename=settings.LOG_FILE)

ch.setFormatter(CustomFormatter())
fh.setFormatter(CustomFormatter())


logger.addHandler(ch)  # 将日志输出至屏幕
logger.addHandler(fh)  # 将日志输出至文件
