from flask import Flask, request
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    logger.info(f"Request: {request.method} {request.url}")
    return 'Hello, World! This is my DevOps project.'

@app.route('/health')
def health():
    logger.info("Health check requested")
    return 'OK', 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    logger.info(f"Starting app on port {port}")
    app.run(host='0.0.0.0', port=port)