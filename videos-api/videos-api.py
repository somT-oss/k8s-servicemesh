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

# GET route for video
@app.route('/get-video/<video>', methods=['GET'])
def get_video(video):

    # Redis DB connection object
    redis_db = connect(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))

    # Error handling for connection failure to Redis
    if redis_db is None: 
        return {
            "message": "Could not connect to DB!",
            "statusCode": 400
        }
    
    # Get video in the DB by using the video_id
    video = redis_db.hgetall(video)
    
    # Return video from the DB
    return {
        "video": video, 
        "statusCode": 200
    }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)