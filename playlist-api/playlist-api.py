from flask import Flask, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import ast
import uuid
import requests
from pprint import pprint
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

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

def get_video(video):
    response = requests.get(f"http://localhost:5001/get-video/{video}")
    return response.json()


@app.route('/create-playlist', methods=['POST'])
def create_new_playlist():
    playlist_id = str(uuid.uuid4())
    videos = request.json['video_id(s)']
    title = request.json['title']
    description = request.json['description']
    date_created = datetime.now()

    playlist_dict = {
        "_id": playlist_id,
        "title": title,
        "description": description,
        "videos": videos,
        "date_created": date_created
    }

    db_connection = connect(URI)
    if db_connection is None:
        return {
            "message": "Could not connect to DB!",
            "statusCode": 400
        }
    
    db = db_connection['playlist-db']
    playlist_db = db['playlist-collection']
    try:
        playlist_db.insert_one(playlist_dict)
        return {
            "message": "Playlist successfully created",
            "statusCode": 200
        }
    except Exception as e:
        return {
            "message": e,
            "statusCode": 400
        }


@app.route('/get-playlists', methods=['GET'])
def get_all_playlists():

    db_connection = connect(URI)
    if db_connection is None:
        return {
            "message": "Could not connect to DB!",
            "statusCode": 400
        }
    
    db = db_connection['playlist-db']
    playlist_db = db['playlist-collection']
    all_playlists = []

    for playlists in playlist_db.find():
        all_playlists.append(playlists)

    return all_playlists    

@app.route('/get-playlists-n-videos', methods=['GET'])
def get_all_playlists_and_video_metadata():
    db_connection = connect(URI)
    if db_connection is None:
        return {
            "message": "Could not connect to DB!",
            "statusCode": 400
        }
    
    db = db_connection['playlist-db']
    playlist_db = db['playlist-collection']

    all_playlist = []
    grouped_videos = []

    for playlists in playlist_db.find():
        for video in ast.literal_eval(playlists["videos"]):
            video_output = get_video(video)
            grouped_videos.append(video_output)
    #     all_playlist.append(playlists)
    
    pprint(grouped_videos)

    return {
        "message": "Done"
    }



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)