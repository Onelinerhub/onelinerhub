# Script

How do I use jQuery and JavaScript together?
// plain

You can use jQuery and JavaScript together to create powerful web applications. jQuery is a JavaScript library that provides an easy way to manipulate the DOM and make AJAX requests. JavaScript is a scripting language that is used to create dynamic web pages.

For example, you can use jQuery and JavaScript together to create a simple web page that displays an alert when a button is clicked.

```
<html>
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script>
    $(document).ready(function(){
      $("button").click(function(){
        alert("Hello World!");
      });
    });
  </script>
</head>
<body>
  <button>Click Me</button>
</body>
</html>
```

When the button is clicked, the following output is displayed:

```
Hello World!
```

The code consists of the following parts:

1. The `<script>` tag with the jQuery library, which provides methods to manipulate the DOM and make AJAX requests.
2. The `$(document).ready()` function, which ensures that the code is executed when the DOM is ready.
3. The `$("button").click()` function, which is triggered when the button is clicked.
4. The `alert("Hello World!")` function, which displays an alert with the text "Hello World!".

For more information on how to use jQuery and JavaScript together, see the following links:

- [jQuery API Documentation](https://api.jquery.com/)
- [JavaScript Tutorial](https://www.w3schools.com/js/)

onelinerhub: [Script

How do I use jQuery and JavaScript together?](https://onelinerhub.com/jquery/script--how-do-i-use-jquery-and-javascript-together)