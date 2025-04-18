import logging
import time
import random
from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - level=%(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/app/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total app HTTP requests')

@app.route('/')
def home():
    # Randomly log different levels
    REQUEST_COUNT.inc()
    log_level = random.choice(['debug', 'warning'])
    if log_level == 'debug':
        logger.debug("This is a debug message - some detailed information")
    else:
        logger.warning("This is a warning message - something might be wrong")
    
    return "Hello, World! Check your logs."

@app.route('/metrics')
def metrics():
    from prometheus_client import generate_latest
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
