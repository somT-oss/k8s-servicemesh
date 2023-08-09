// Function to call the video API with the selected video's ID
function playVideo(videoId) {
  fetch(VIDEO_API_ENDPOINT + '/' + videoId)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      var videoUrl = data.video_url;
      var player = document.getElementById('player');
      player.setAttribute('src', videoUrl);
    })
    .catch(function (error) {
      console.error('Error playing video:', error);
    });
}

// Function to create video items and buttons for a playlist
function displayPlaylist(playlistData) {
  var playlistContainer = document.getElementById('playlist-container');
  var playlistTitle = document.createElement('h2');
  playlistTitle.textContent = playlistData.title;
  playlistContainer.appendChild(playlistTitle);

  var videosList = document.createElement('ul');

  playlistData.videos.forEach(function (videoId) {
    fetch(VIDEO_API_ENDPOINT + '/' + videoId)
      .then(function (response) {
        return response.json();
      })
      .then(function (videoData) {
        // Create a list item for each video
        var videoItem = document.createElement('li');
        videoItem.textContent = videoData.title; // Assuming the API response contains the video title as 'title'

        var playButton = document.createElement('button');
        playButton.textContent = 'Play Video';
        playButton.addEventListener('click', function () {
          playVideo(videoData._id); // Assuming the video ID is available as '_id'
        });

        videoItem.appendChild(playButton);
        videosList.appendChild(videoItem);
      })
      .catch(function (error) {
        console.error('Error fetching video:', error);
      });
  });

  playlistContainer.appendChild(videosList);
}

// Function to fetch playlists from the API
function fetchPlaylists() {
  fetch(API_ENDPOINT)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Assuming the API response is an array of playlists
      data.forEach(function (playlist) {
        displayPlaylist(playlist);
      });
    })
    .catch(function (error) {
      console.error('Error fetching playlists:', error);
    });
}
// Function to call the video API with the selected video's ID
function playVideo(videoId) {
  fetch(VIDEO_API_ENDPOINT + '/' + videoId)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Assuming the API response contains the video URL
      var videoUrl = data.video_url; // Assuming the API response contains the video URL as 'video_url'
      var player = document.getElementById('player');
      player.setAttribute('src', videoUrl);
    })
    .catch(function (error) {
      console.error('Error playing video:', error);
    });
}

// Function to create video items and buttons for a playlist
function displayPlaylist(playlistData) {
  var playlistContainer = document.getElementById('playlist-container');
  var playlistTitle = document.createElement('h2');
  playlistTitle.textContent = playlistData.title;
  playlistContainer.appendChild(playlistTitle);

  var videosList = document.createElement('ul');

  playlistData.videos.forEach(function (videoId) {
    fetch(VIDEO_API_ENDPOINT + '/' + videoId)
      .then(function (response) {
        return response.json();
      })
      .then(function (videoData) {
        // Create a list item for each video
        var videoItem = document.createElement('li');
        videoItem.textContent = videoData.title; // Assuming the API response contains the video title as 'title'

        var playButton = document.createElement('button');
        playButton.textContent = 'Play Video';
        playButton.addEventListener('click', function () {
          playVideo(videoData._id); // Assuming the video ID is available as '_id'
        });

        videoItem.appendChild(playButton);
        videosList.appendChild(videoItem);
      })
      .catch(function (error) {
        console.error('Error fetching video:', error);
      });
  });

  playlistContainer.appendChild(videosList);
}

// Function to fetch playlists from the API
function fetchPlaylists() {
  fetch(API_ENDPOINT)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Assuming the API response is an array of playlists
      data.forEach(function (playlist) {
        displayPlaylist(playlist);
      });
    })
    .catch(function (error) {
      console.error('Error fetching playlists:', error);
    });
}
