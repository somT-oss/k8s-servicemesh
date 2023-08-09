//set the APIs here
window.process = {
  env: {
    REACT_APP_PLAYLIST_API_URL: 'http://127.0.0.1:5000/get-playlists',
    REACT_APP_VIDEO_API_URL: 'http://127.0.0.1:5001/<video_id>'
  }
};
