# How do I use the jQuery ready function?
// plain

The jQuery `ready()` function is used to execute code when the DOM is fully loaded. This is useful when you want to make sure that all elements on the page are available before running your script.

```
$(document).ready(function(){
  alert("The page is ready!");
});
```

## Output example

```
Alert message: The page is ready!
```

The code above will execute the `alert()` function when the DOM is ready.

Here's a breakdown of the code:

- `$(document)`: This is a jQuery selector that selects the `document` object.
- `.ready()`: This is a jQuery method that is used to execute code when the DOM is ready.
- `function(){`: This is an anonymous function that contains the code to be executed when the DOM is ready.
- `alert("The page is ready!");`: This is the code that will be executed when the DOM is ready.
- `});`: This is the closing brace for the anonymous function.

For more information about the jQuery `ready()` function, please refer to the following link:

- [jQuery Documentation: ready()](https://api.jquery.com/ready/)

onelinerhub: [How do I use the jQuery ready function?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-ready-function)