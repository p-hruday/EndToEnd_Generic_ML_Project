import os
import logging
from datetime import datetime

# Create the log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Set the path to the 'logs' directory under the current working directory
log_dir = os.path.join(os.getcwd(), "logs")
# Ensure the 'logs' directory exists
os.makedirs(log_dir, exist_ok=True)
# Create the full log file path
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

'''
if __name__ == "__main__":
    logging.info("Logging has started")
'''