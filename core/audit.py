import logging

logger = logging.getLogger("audit")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

class AuditLogger:
    """Audit logger that writes to Cloud Logging via stdout."""

    @staticmethod
    def log(message: str, filename: str = ""):
        if filename:
            logger.info(f"{message} - file: {filename}")
        else:
            logger.info(message)
