# How do I use jQuery to create a simple example?
// plain

jQuery is a JavaScript library that makes it easy to manipulate the DOM (Document Object Model) of a webpage. To create a simple example using jQuery, you can use the following code:

```
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script>
      $(document).ready(function(){
        $("#btn1").click(function(){
          $("#div1").text("Hello World!");
        });
      });
    </script>
  </head>
  <body>
    <div id="div1"></div>
    <button id="btn1">Click Me</button>
  </body>
</html>
```

This code will create a webpage with a button and an empty div. When the button is clicked, the text "Hello World!" will appear in the div.

The code is composed of the following parts:

1. The jQuery library is imported from a CDN (Content Delivery Network).
2. An anonymous function is declared and called when the document is ready.
3. An event listener is attached to the button to listen for a click.
4. When the button is clicked, the text "Hello World!" is inserted into the div.

For more information about jQuery, you can refer to the official [jQuery Documentation](https://api.jquery.com/).

onelinerhub: [How do I use jQuery to create a simple example?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-create-a-simple-example)