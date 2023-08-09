from flask import Flask, request
from redis import Redis
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})


def connect(host, port): 
    redis_db = Redis(host=host, port=port, decode_responses=True)

    return redis_db


@app.route('/get-video/<video>', methods=['GET'])
def get_video(video):

    redis_db = connect(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))

    if redis_db is None: 
        return {
            "message": "Could not connect to DB!",
            "statusCode": 400
        }
    
    video = redis_db.hgetall(video)
    return {
        "video": video, 
        "statusCode": 200
    }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)