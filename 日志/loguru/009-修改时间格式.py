import sys
from loguru import logger

logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
