from redis import Redis
import uuid
from datetime import datetime
import time
import os
from pprint import pprint

def connect(host, port): 
    redis_db = Redis(host=host, port=port, decode_responses=True)

    return redis_db


def add_playlists(): 
    redis_db = connect(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))

    if redis_db is None:
        print("Error occurred trying to connect to DB")

    redis_db.hset(
        "playlist:1", mapping={
            'title': "Tech Videos",
            'description': "This is a tech video playlist",
            "playlist_id": str(uuid.uuid4()),
            "videos": "['video 1']",
            "date_created ": str(datetime.now())
        }
    )

    print("Finished adding playlist 1...")
    time.sleep(2)

    redis_db.hset(
        "playlist:2", mapping={
            'title': "Crypto Videos",
            'description': "This is a crypto video playlist",
            "playlist_id": str(uuid.uuid4()),
            "videos": "['video 11']",
            "date_created ": str(datetime.now())
        }
    )

    print("Finished adding playlist 2...")
    time.sleep(2)

    redis_db.hset(
        "playlist:3", mapping={
            'title': "Workout Videos",
            'description': "This is a workout video playlist",
            "playlist_id": str(uuid.uuid4()),
            "videos": "['video 21']",
            "date_created ": str(datetime.now())
        }
    )

    print("Finished adding playlist 3...")
    print("Done with adding all playlists")


def add_videos():
    redis_db = connect(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))

    if redis_db is None:
        return "Error occurred trying to connect to DB"

    redis_db.hset(
        "video-1", mapping={
            'title': "New iPhone",
            'description': "New iPhone out now",
            "video_id": str(uuid.uuid4()),
            "date_created ": str(datetime.now())
        }
    )

    print("Finished adding video 1...")
    time.sleep(2)

    redis_db.hset(
        "video-11", mapping={
            'title': "FOMO BTC",
            'description': "Trade BTC now",
            "video_id": str(uuid.uuid4()),
            "date_created ": str(datetime.now())
        }
    )

    print("Finished adding video 2...")
    time.sleep(2)

    redis_db.hset(
        "video-21", mapping={
            'title': "Workout ABS",
            'description': "Start taining your abs now",
            "video_id": str(uuid.uuid4()),
            "date_created ": str(datetime.now())
        }
    )

    print("Finished adding video 3...")
    print("Done with adding all videos")


def main():

    add_playlists()
    add_videos()

if __name__ == "__main__":
    main()