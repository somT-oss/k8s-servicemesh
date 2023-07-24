from flask import Flask, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import uuid
import ast
import os

app = Flask(__name__)

URI = f"mongodb+srv://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@k8s-cluster-db.qjpa5yf.mongodb.net/?retryWrites=true&w=majority"


def connect(URI: str): 
    # Set the Stable API version when creating a new client
    client = MongoClient(URI, server_api=ServerApi('1'))
                            
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        return client
    except Exception as e:
        print(e)
        return None


@app.route("/create-video", methods=['POST'])
def create_videos():
    video_uuid = str(uuid.uuid4())
    video = videos_in_tech[2]
    title = request.json['title']
    description = request.json['description']
    date_created = datetime.now()

    video_dict = {
        "_id": video_uuid,
        "title": title,
        "video": video,
        "description": description,
        "date_created": date_created
    }

    db_connection = connect(URI)
    if db_connection is None:
        return {
            "message": "Could not connect to DB!",
            "statusCode": 400
        }
        
    db = db_connection['videos-db']
    videos_db = db['videos-collection']
    try:
        videos_db.insert_one(video_dict)
        return {
            "message": "Video successfully created",
            "statusCode": 200
        }
    except Exception as e:
        return {
            "message": e,
            "statusCode": 400
        }

@app.route('/get-video/<video>', methods=['GET'])
def get_video(video):

    db_connection = connect(URI)
    if db_connection is None:
        return {
            "message": "Could not connect to DB!",
            "statusCode": 400
        }
    
    db = db_conn['videos-db']
    videos_db = db['videos-collection']

    try:
        video = videos_db.find_one({"video": video})
        return video
    except Exception as e:
        print("Error: ", e, " occurred")
        return {
            "message": "An error occurred",
            "statusCode": 400
        }


if __name__ == '__main__':
    app.run(port=5001, debug=True)