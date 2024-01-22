from flask import Flask
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

app.run(host='0.0.0.0', port=8080)
