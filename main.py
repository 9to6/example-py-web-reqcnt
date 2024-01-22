from flask import Flask
import os
import asyncio

counter_lock = asyncio.Lock()
counter = 0

app = Flask(__name__)

@app.route('/')
@app.route('/reqcnt/')
async def index():
    global counter

    async with counter_lock:
        counter += 1
    return 'Web App with Python Flask! - {}'.format(counter)

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '5000')
    app.run(host=host, port=int(port))
