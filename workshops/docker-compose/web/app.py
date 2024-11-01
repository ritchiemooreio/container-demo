# web/app.py
from flask import Flask
import os
import redis

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_client = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/')
def hello():
    # Increment counter
    count = redis_client.incr('hits')
    return f"Hello! You've visited this page {count} times.\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
