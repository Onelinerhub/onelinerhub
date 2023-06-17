# How can I use jQuery to zoom an image when the user hovers over it?
// plain

Using jQuery, you can easily zoom an image when the user hovers over it. The following example code shows how to do this:
```
$(document).ready(function(){
  $("img").hover(function(){
    $(this).css("transform", "scale(1.2)");
  },
  function(){
    $(this).css("transform", "scale(1)");
  });
});
```
In this code, the `$(document).ready()` function is used to ensure that the code runs when the page is ready. Then, the `$("img")` selector is used to select all img elements on the page. The `.hover()` method is then used to specify two functions to run when the user hovers over the image. The first function is used to increase the size of the image by applying a `transform: scale(1.2)` CSS rule to it, while the second function is used to reset the size of the image when the user moves the mouse away from it.

## Code explanation

- `$(document).ready()`: This function is used to ensure that the code runs when the page is ready.
- `$("img")`: This selector is used to select all img elements on the page.
- `.hover()`: This method is used to specify two functions to run when the user hovers over the image.
- `transform: scale(1.2)`: This CSS rule is used to increase the size of the image.
- `transform: scale(1)`: This CSS rule is used to reset the size of the image.

## Helpful links
- [jQuery Documentation](https://api.jquery.com/)
- [CSS Transform Property](https://www.w3schools.com/cssref/css3_pr_transform.asp)

onelinerhub: [How can I use jQuery to zoom an image when the user hovers over it?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-zoom-an-image-when-the-user-hovers-over-it)