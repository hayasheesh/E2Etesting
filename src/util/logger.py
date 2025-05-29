import logging
import allure
from datetime import datetime

# Setup logging with timestamped filename
LOG_FILE = f"test_log_{datetime.now().strftime("%d%m%y_%H%M")}.txt"
logging.basicConfig(
    level=logging.DEBUG,  # Capture all logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),  # Log to file
        logging.StreamHandler()  # Log to console
    ],
)

LOGGER = logging.getLogger()

def log_to_allure(message, level="info"):
    """Logs messages to both the log file and Allure report."""
    if level == "info":
        LOGGER.info(message)
        allure.attach(message, name="Log Info", attachment_type=allure.attachment_type.TEXT)
    elif level == "warning":
        LOGGER.warning(message)
        allure.attach(message, name="Log Warning", attachment_type=allure.attachment_type.TEXT)
    elif level == "error":
        LOGGER.error(message)
        allure.attach(message, name="Log Error", attachment_type=allure.attachment_type.TEXT)
