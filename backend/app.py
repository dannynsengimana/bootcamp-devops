from flask import Flask, request, jsonify
from flask_cors import CORS
import redis
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for local development

redis_host = os.environ.get('REDIS_HOST', 'redis-service')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_password = os.environ.get('REDIS_PASSWORD')  # Get password from env

redis_client = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password  # Pass password to Redis client
)

@app.route('/api/modules', methods=['POST', 'GET'])
def modules():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'module' not in data:
            return jsonify({'error': 'Missing module'}), 400
        module = data['module']
        redis_client.rpush('modules', json.dumps(module))
        return jsonify({'message': 'Module added'}), 201
    else:
        modules = redis_client.lrange('modules', 0, -1)
        decoded_modules = [json.loads(msg.decode('utf-8')) for msg in messages]
        return jsonify(decoded_modules)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)