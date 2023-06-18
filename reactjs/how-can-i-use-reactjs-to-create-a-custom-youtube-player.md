# How can I use ReactJS to create a custom YouTube player?
// plain

You can use ReactJS to create a custom YouTube player by using the YouTube Data API and the `react-youtube` package.

```
import React from 'react'
import YouTube from 'react-youtube'

class YouTubePlayer extends React.Component {
  render() {
    const opts = {
      height: '390',
      width: '640',
      playerVars: {
        // https://developers.google.com/youtube/player_parameters
        autoplay: 1,
      },
    };

    return (
      <YouTube
        videoId="2g811Eo7K8U"
        opts={opts}
        onReady={this._onReady}
      />
    );
  }

  _onReady(event) {
    // access to player in all event handlers via event.target
    event.target.pauseVideo();
  }
}
```

The code above will render a YouTube video with the ID `2g811Eo7K8U` and will set the player's height and width to `390` and `640` respectively. The `playerVars` option will set the autoplay to `1` so that the video will autoplay when it is rendered. The `_onReady` event handler will pause the video when it is finished loading.

Parts of the code:

- `import React from 'react'`: imports the React library
- `import YouTube from 'react-youtube'`: imports the `react-youtube` package
- `class YouTubePlayer extends React.Component`: creates the `YouTubePlayer` class which inherits from the `React.Component` class
- `const opts`: creates an `opts` object which contains the options for the YouTube player
- `return ( <YouTube videoId="2g811Eo7K8U" opts={opts} onReady={this._onReady} /> )`: renders the YouTube player with the `videoId` and `opts` object, and passes the `_onReady` event handler
- `_onReady(event) { event.target.pauseVideo() }`: event handler which pauses the video when it is finished loading

## Helpful links

- [YouTube Data API](https://developers.google.com/youtube/v3)
- [react-youtube](https://www.npmjs.com/package/react-youtube)
- [YouTube Player Parameters](https://developers.google.com/youtube/player_parameters)

onelinerhub: [How can I use ReactJS to create a custom YouTube player?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-to-create-a-custom-youtube-player)