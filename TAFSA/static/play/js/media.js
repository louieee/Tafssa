const videoTag = document.getElementById("my-video");

// creating the MediaSource, just with the "new" keyword, and the URL for it
const myMediaSource = new MediaSource();
const url = URL.createObjectURL(myMediaSource);

// attaching the MediaSource to the video tag
videoTag.src = url;