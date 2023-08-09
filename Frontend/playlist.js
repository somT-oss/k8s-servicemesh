const playlistsContainer = document.getElementById('playlists');
const videosContainer = document.getElementById('videos');

async function fetchPlaylists() {
  try {
    const response = await fetch(PLAYLIST_API_ENDPOINT);
    const playlists = await response.json();
    renderPlaylists(playlists);
  } catch (error) {
    console.error('Error fetching playlists:', error);
  }
}

async function fetchVideos(videoIds) {
  const videoPromises = videoIds.map(async videoId => {
    const response = await fetch(`${VIDEO_API_ENDPOINT}/${videoId}`);
    return response.json();
  });

  try {
    const videos = await Promise.all(videoPromises);
    renderVideos(videos);
  } catch (error) {
    console.error('Error fetching videos:', error);
  }
}

function renderPlaylists(playlists) {
  playlistsContainer.innerHTML = '';
  playlists.forEach(playlist => {
    const playlistDiv = document.createElement('div');
    playlistDiv.classList.add('playlist');

    const playlistInfo = `
      <h2>${playlist.title}</h2>
      <p>${playlist.description}</p>
      <button class="watchBtn" data-videos="${JSON.stringify(playlist.videos)}">Watch Playlist</button>
    `;

    playlistDiv.innerHTML = playlistInfo;
    playlistsContainer.appendChild(playlistDiv);
  });

  const watchButtons = document.querySelectorAll('.watchBtn');
  watchButtons.forEach(button => {
    button.addEventListener('click', () => {
      const videoIds = JSON.parse(button.getAttribute('data-videos'));
      fetchVideos(videoIds);
    });
  });
}

function renderVideos(videos) {
  videosContainer.innerHTML = '';
  videos.forEach(video => {
    const videoDiv = document.createElement('div');
    videoDiv.classList.add('video');

    const videoInfo = `
      <h2>${video.title}</h2>
      <p>${video.description}</p>
      <video controls>
        <source src="${video.video}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    `;

    videoDiv.innerHTML = videoInfo;
    videosContainer.appendChild(videoDiv);
  });
}

fetchPlaylists();
