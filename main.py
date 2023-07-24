import requests as r
import json
from pprint import pprint
import ast

def get_video(video):
    response = r.get(f"http://localhost:5001/get-video/{video}")
    return response.json()

response = r.get("http://127.0.0.1:5000/get-playlists")

grouped_videos = []

for playlist in response.json():
    for video in ast.literal_eval(playlist["videos"]):
        video_output = get_video(video)
        grouped_videos.append(video_output)

        pprint(grouped_videos)