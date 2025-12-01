import logging

# Configure a logger that writes to stdout (Cloud Run streams this to Cloud Logging)
logger = logging.getLogger("audit")
logger.setLevel(logging.INFO)

# Ensure logs propagate to the root logger
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def log(message: str, filename: str = ""):
    """Log audit events to Cloud Logging instead of a local file."""
    if filename:
        logger.info(f"{message} - file: {filename}")
    else:
        logger.info(message)
