# k8s-servicemesh

This is a simple project highlighting how to setup a servicemesh for your services in a Kubernetes cluster.

This project was inspired from [Marcel Damper's servicemesh project](https://github.com/marcel-dempers/docker-development-youtube-series/blob/master/kubernetes/servicemesh/introduction.md). It's a replica, more or less. I am looking to further develop this project by deploying it to AWS or any other Cloud Service Platform. 









## Architecture

The application as a whole consists of 3 different services
* Playlists API.
* Video API.
* Frontend application. 

The backend is primarily handled by both the Playlists and Video API respectively. 

Each API has a seperate Database. The Database is hosted on Mongo Atlas. 

The Frontend Application sends an API request to the Playlist API which returns a JSON response:
```
{
    "_id": "video_uuid",
    "date_created": "Date Playlist was created",
    "description": "Playlist Description",
    "title": "Playlist title",
    "videos": "['video_1', 'video_2', 'video_3']"
}
```

Each video in this response does not correspond to a whole video. It is a ```video_id```. 
This ```video_id``` can be passed to the Video API to get information about that video.

The response from the Video API looks like this: 
```
{
    "_id": "video_uuid",
    "date_created": "Date Video was created",
    "description": "Video description",
    "title": "Video title",
    "video": "video_id"
}
```

[//]: # (Add architecture image)


## Tools
* Minikube
* Istio
* Flask
