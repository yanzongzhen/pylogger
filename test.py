from logger import InitLogConfig
import logger
import logging

InitLogConfig(loglevel=logging.INFO)

logger.debug("DEBUG")
logger.info("INFO")
logger.error("INFO")
logger.warning("INFO")
logger.fatal("INFO")
