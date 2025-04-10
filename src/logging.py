import logging
from logging.handlers import RotatingFileHandler
import os

# Ensure log directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configure log file path
LOG_FILE = os.path.join(LOG_DIR, "threat_events.log")

# Setup Rotating File Handler
handler = RotatingFileHandler(
    LOG_FILE, maxBytes=1024 * 1024, backupCount=5
)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Setup logger
logger = logging.getLogger("ThreatLogger")
logger.setLevel(logging.INFO)

# Add handler if not already added
if not logger.handlers:
    logger.addHandler(handler)

def log_threat(threat: str, risk_score: int):
    """
    Logs a threat event with detailed info.
    """
    logger.info(f"Threat Detected | Type: {threat} | Risk Score: {risk_score}")

# Example usage (for testing/demo only)
if __name__ == "__main__":
    log_threat("DDoS Attack", 30)
