# How can I use jQuery to embed a YouTube video on my website?
// plain

Using jQuery to embed a YouTube video on a website is a fairly straightforward process. Here is an example code block that can be used to accomplish this:
```
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  </head>
  <body>
    <div id="player"></div>
    <script>
      $(document).ready(function() {
        $("#player").html('<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>');
      });
    </script>
  </body>
</html>
```

This code block will embed a YouTube video into the `<div>` element with the id of "player". The `VIDEO_ID` portion of the code should be replaced with the ID of the video to be embedded.

The code consists of the following parts:
1. An HTML document with a `<head>` and `<body>` section.
2. A `<script>` tag that links to jQuery.
3. A `<div>` element with an id of "player".
4. A `<script>` tag that contains a jQuery code block.

The jQuery code block consists of the following parts:
1. `$(document).ready(function() {...})` - This code ensures that the code inside the function will run after the page has finished loading.
2. `$("#player").html('<iframe...>');` - This code replaces the content of the `<div>` element with an id of "player" with an `<iframe>` element containing the YouTube video.

For more information on jQuery and embedding YouTube videos, please refer to the following links:
1. [jQuery Documentation](https://api.jquery.com/)
2. [YouTube Embedded Players and Player Parameters](https://developers.google.com/youtube/player_parameters)

onelinerhub: [How can I use jQuery to embed a YouTube video on my website?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-embed-a-youtube-video-on-my-website)