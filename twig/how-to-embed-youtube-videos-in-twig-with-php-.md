# How to embed YouTube videos in Twig with PHP?
// plain

Embedding YouTube videos in Twig with PHP is a simple process. The following example code block will demonstrate how to do this:
```
<div class="video-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/{{ video_id }}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```
The output of this code will be an embedded YouTube video:

<div class="video-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/{{ video_id }}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Code explanation

- `<div class="video-container">`: This is the container element for the video.
- `<iframe width="560" height="315" src="https://www.youtube.com/embed/{{ video_id }}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`: This is the iframe element that contains the YouTube video. The `{{ video_id }}` should be replaced with the ID of the YouTube video.

## Helpful links
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [YouTube Embed Code Generator](https://www.embed-code-generator.com/youtube.html)

onelinerhub: [How to embed YouTube videos in Twig with PHP?](https://onelinerhub.com/twig/how-to-embed-youtube-videos-in-twig-with-php-)