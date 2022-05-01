import sys
from loguru import logger

# loguru支持f-string：
logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")
