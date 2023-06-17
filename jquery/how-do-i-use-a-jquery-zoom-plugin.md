# How do I use a jQuery zoom plugin?
// plain

To use a jQuery zoom plugin, you first need to include the jQuery library and the plugin's JavaScript and CSS files in the head of your HTML document.

```
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="jquery.zoom.js"></script>
  <link rel="stylesheet" type="text/css" href="jquery.zoom.css">
</head>
```

Then, you need to call the `.zoom()` method on the desired element, such as an image.

```
<script>
  $(document).ready(function(){
    $('#myImage').zoom();
  });
</script>
```

You can also customize the plugin by passing additional options as an object to `.zoom()`, such as `magnify`, which sets the zoom level.

```
<script>
  $(document).ready(function(){
    $('#myImage').zoom({magnify: 2});
  });
</script>
```

This will double the zoom level of the image.

You can find more information about the jQuery zoom plugin here:
- [jQuery Zoom Plugin](https://www.jqueryscript.net/zoom/Simple-jQuery-Zoom-Plugin.html)
- [jQuery Zoom Documentation](https://dimsemenov.com/plugins/magnific-popup/documentation.html)

onelinerhub: [How do I use a jQuery zoom plugin?](https://onelinerhub.com/jquery/how-do-i-use-a-jquery-zoom-plugin)