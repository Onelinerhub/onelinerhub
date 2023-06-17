# How do I implement a jQuery lightbox?
// plain

A jQuery lightbox is a script that allows you to display images and other web content in a pop-up window. To implement a jQuery lightbox, you will need to include the jQuery library in your HTML page, and then create a link to the jQuery lightbox script.

You can use the following code to include the jQuery library and lightbox script in your HTML page:
```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="js/jquery.lightbox.js"></script>
```

Then, you will need to create the HTML markup for the lightbox. This can be done by adding a link to the image you want to display in the lightbox, and then adding a div element with the class 'lightbox' to the page:

```
<a href="image.jpg" class="lightbox">
  <img src="thumbnail.jpg" alt="My Image" />
</a>
<div class="lightbox">
  <img src="image.jpg" alt="My Image" />
</div>
```

Finally, you will need to add some jQuery code to initialize the lightbox. This can be done by selecting the link and div elements, and then calling the lightbox() method on them:

```
$(document).ready(function() {
  $('.lightbox').lightbox();
});
```

This will create a lightbox that displays the image when the link is clicked.

## Helpful links
- [jQuery Lightbox](https://github.com/duncanmcdougall/Responsive-Lightbox)
- [jQuery Documentation](https://api.jquery.com/)

onelinerhub: [How do I implement a jQuery lightbox?](https://onelinerhub.com/jquery/how-do-i-implement-a-jquery-lightbox)