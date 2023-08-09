from flask import Flask, request
from redis import Redis
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

def connect(host, port): 
    redis_db = Redis(host=host, port=port, decode_responses=True)

    return redis_db


@app.route('/get-playlists', methods=['GET'])
def get_all_playlists():

    redis_db = connect(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))

    if redis_db is None: 
        return {
            "message": "Could not connect to DB!",
            "statusCode": 400
        }
    

    if redis_db is None:
        return "Error occurred trying to connect to DB"
    
    hash_keys = ['playlist:1', 'playlist:2', 'playlist:3']
    playlists = []

    for key in hash_keys:
        data = redis_db.hgetall(key)
        playlists.append(data)
    
    return {
        "playlists": playlists,
        "statusCode": 200
    }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)