import logging
import os
import sys
from functools import wraps
from time import time
from typing import Callable

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "[%(filename)s:%(lineno)d] :%(levelname)8s: %(message)s"
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))

log_level = getattr(logging, LOG_LEVEL, logging.INFO)
logger = logging.getLogger()

for h in logger.handlers:
    logger.removeHandler(h)

logger.addHandler(stream_handler)
logger.setLevel(log_level)


def log_function(func: Callable) -> Callable:
    @wraps(func)
    def wrap_func(*args, **kwargs):
        logger.info(f"[FUNCTION][{func.__name__}()] start.")
        start_time = time()
        result_func = func(*args, **kwargs)
        execute_time = round(time() - start_time, 3)
        logger.info(f"[FUNCTION][{func.__name__}()] time executed={execute_time}s.")
        return result_func

    return wrap_func
