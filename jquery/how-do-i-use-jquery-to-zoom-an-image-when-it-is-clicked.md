# How do I use jQuery to zoom an image when it is clicked?
// plain

To use jQuery to zoom an image when it is clicked, first you must include the jQuery library in your HTML file.

```<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>```

Then, you can use the following jQuery code to zoom the image when it is clicked:

```
$(document).ready(function(){
  $("img").click(function(){
    $(this).animate({width: "500px", height: "500px"});
  });
});
```

This code will make the image zoom to 500px by 500px when it is clicked.

The code consists of the following parts:

* `$(document).ready(function()` - this is a jQuery method that will run the code when the document is ready.
* `$("img")` - this is a jQuery selector that will select all `<img>` tags.
* `.click(function()` - this is a jQuery method that will run the code when the image is clicked.
* `$(this)` - this is a jQuery selector that will select the image that was clicked.
* `.animate({width: "500px", height: "500px"})` - this is a jQuery method that will animate the selected image to 500px by 500px.

## Helpful links

* [jQuery Documentation](https://api.jquery.com/)
* [jQuery .ready() Method](https://api.jquery.com/ready/)
* [jQuery Selectors](https://api.jquery.com/category/selectors/)
* [jQuery .click() Method](https://api.jquery.com/click/)
* [jQuery .animate() Method](https://api.jquery.com/animate/)

onelinerhub: [How do I use jQuery to zoom an image when it is clicked?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-zoom-an-image-when-it-is-clicked)