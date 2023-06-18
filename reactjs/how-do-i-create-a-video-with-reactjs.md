# How do I create a video with ReactJS?
// plain

Creating a video with ReactJS is possible with a few lines of code. The following example code uses the `<video>` element to render a video in the browser:

```
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4" />
</video>
```

This code will render a video element with the width of 320px and the height of 240px. The `controls` attribute adds the controls for the video, such as play/pause and volume control. The `<source>` element is used to specify the source of the video, which can be an mp4, ogg, or webm file.

To add the video to a React component, you can use the `<video>` element in the `render()` method. For example:

```
render() {
  return (
    <video width="320" height="240" controls>
      <source src="movie.mp4" type="video/mp4" />
    </video>
  );
}
```

This will render the video as part of the React component. You can also add additional attributes to the `<video>` element, such as `autoplay` or `loop`.

For more information on working with videos in React, see the [official React documentation](https://reactjs.org/docs/dom-elements.html#media-elements).

onelinerhub: [How do I create a video with ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-a-video-with-reactjs)