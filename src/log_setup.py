import os
import logging

# Logging configuration
LOGS_DIR = 'logs'
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, 'dashboard.log')

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(name)s] - %(message)s',
)

# Print logs to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(name)s] - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logging.getLogger("httpx").setLevel(logging.WARNING)