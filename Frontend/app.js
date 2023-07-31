function fetchPlaylists() {
  const playlistUrl = process.env.REACT_APP_PLAYLIST_API_URL;
  const videoUrl = process.env.REACT_APP_VIDEO_API_URL;

  //Promise.all() fetches both playlist and video APIs concurrently
  Promise.all([fetch(playlistUrl), fetch(videoUrl)])
    .then(([playlistResponse, videoResponse]) => {
      if (!playlistResponse.ok) {
        throw new Error('Failed to fetch playlists');
      }
      if (!videoResponse.ok) {
        throw new Error('Failed to fetch videos');
      }
      return Promise.all([playlistResponse.json(), videoResponse.json()]);
    })
    .then(([playlistsData, videosData]) => {
      // This processes playlists and videos data as needed then displays it
      const playlists = processPlaylistsData(playlistsData);
      const videos = processVideosData(videosData);

      displayPlaylistsAndVideos(playlists, videos);
    })
    .catch(error => console.error(error));
}

function processPlaylistsData(playlistsData) {
  return playlistsData.map(playlist => ({
    _id: playlist.playlist_id,
    title: playlist.title,
    description: playlist.description,
    videos: [], 
    date_created: playlist.date_created,
  }));
}

function processVidposData(videosData) {
  return videosData.map(video => ({
    _id: video.video_uuid,
    date_created: video.date_created,
    description: video.description,
    title: video.video_title,
    video: video.video_id
  }));
}

function displayPlaylistsAndVideos(playlists, videos) {
  const playlistContainer = document.getElementById('playlist-container');
  playlistContainer.innerHTML = '';

  playlists.forEach(playlist => {
    const playlistElement = document.createElement('div');
    playlistElement.classList.add('playlist');
    playlistElement.dataset.id = playlist._id;

    const titleElement = document.createElement('h3');
    titleElement.textContent = playlist.title;

    const descriptionElement = document.createElement('p');
    descriptionElement.textContent = playlist.description;

    const videosElement = document.createElement('p');
    videosElement.textContent = `Videos: ${playlist.videos.join(', ')}`;
    videosElement.classList.add('videos');

    const dateElement = document.createElement('p');
    dateElement.textContent = `Date Created: ${playlist.date_created}`;

    playlistElement.appendChild(titleElement);
    playlistElement.appendChild(descriptionElement);
    playlistElement.appendChild(videosElement);
    playlistElement.appendChild(dateElement);

    playlistContainer.appendChild(playlistElement);
  });

  // Update playlists with their associated videos
  playlists.forEach(playlist => {
    playlist.videos = videos.filter(video => video.video === playlist._id).map(video => video.title);
  });

  // Update displayed videos for each playlist
  playlists.forEach(playlist => {
    const playlistElement = playlistContainer.querySelector(`[data-id="${playlist._id}"] .videos`);
    playlistElement.textContent = `Videos: ${playlist.videos.join(', ')}`;
  });
}
