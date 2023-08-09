from flask import Flask, request
from redis import Redis
import os
from flask_cors import CORS

# Flask app
app = Flask(__name__)

# CORS configuration
CORS(app, resources={r"*": {"origins": "*"}})

# Redis DB connection function
def connect(host, port): 
    redis_db = Redis(host=host, port=port, decode_responses=True)

    return redis_db

# GET route for all playlists
@app.route('/get-playlists', methods=['GET'])
def get_all_playlists():

    # Redis DB connection object
    redis_db = connect(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))

    # Error handling for connection failure to Redis
    if redis_db is None: 
        return {
            "message": "Could not connect to DB!",
            "statusCode": 400
        }
    

    if redis_db is None:
        return "Error occurred trying to connect to DB"
    
    # All playlist hashes in the redis key value store
    hash_keys = ['playlist:1', 'playlist:2', 'playlist:3']
    playlists = []

    for key in hash_keys:
        data = redis_db.hgetall(key)
        playlists.append(data)
    
    # Return all playlists in the DB
    return playlists


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)