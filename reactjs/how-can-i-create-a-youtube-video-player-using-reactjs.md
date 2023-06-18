# How can I create a YouTube video player using ReactJS?
// plain

Creating a YouTube video player using ReactJS is relatively straightforward. To begin, you will need to obtain the YouTube Data API key from the Google Developer Console. Once you have the API key, you can use the React Player component to embed the YouTube video into your React application.

## Example code

```
import React from 'react';
import ReactPlayer from 'react-player';

const YouTubePlayer = () => {
  return (
    <ReactPlayer
      url={`https://www.youtube.com/watch?v=${API_KEY}`}
      playing
      width='100%'
      height='100%'
    />
  );
};

export default YouTubePlayer;
```

The code above will render the YouTube video player in the browser. It accepts the API key as a parameter, and will automatically play the video.

The code consists of the following parts:

1. `import React from 'react'` - imports the React library into the component.
2. `import ReactPlayer from 'react-player'` - imports the ReactPlayer component from the react-player package.
3. `const YouTubePlayer = () => {...}` - defines the YouTubePlayer component.
4. `<ReactPlayer ... />` - embeds the YouTube video player in the application. It accepts the API key as a parameter, and will automatically play the video.

## Helpful links
- [React Player Documentation](https://www.npmjs.com/package/react-player)
- [YouTube Data API Documentation](https://developers.google.com/youtube/v3/getting-started)

onelinerhub: [How can I create a YouTube video player using ReactJS?](https://onelinerhub.com/reactjs/how-can-i-create-a-youtube-video-player-using-reactjs)