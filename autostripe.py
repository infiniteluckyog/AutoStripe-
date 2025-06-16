from quart import Quart, request, jsonify
import httpx
import asyncio

app = Quart(__name__)

@app.route('/test')
async def test():
    return 'OK'

@app.route('/stripe_raw', methods=['GET'])
async def stripe_raw():
    return jsonify({'success': True})

# Do NOT put `app = "anything"` anywhere else in the file!
