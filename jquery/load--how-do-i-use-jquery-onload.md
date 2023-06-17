# load

How do I use jQuery onload?
// plain

jQuery has a built-in method for running code when the page is loaded, called `$(document).ready()`. This method allows you to run code as soon as the page is ready for manipulation. The syntax is as follows:

```javascript
$(document).ready(function(){
  // Your code here
});
```

The code inside the `$(document).ready()` function will be executed once the page has finished loading. For example, if you wanted to alert a message when the page is loaded, you could do this:

```javascript
$(document).ready(function(){
  alert("Page loaded!");
});
```

This would output the following alert:

```
Page loaded!
```

## Code explanation


- `$(document).ready()`: This is the jQuery method that is used to run code when the page is loaded.
- `function(){...}`: This is an anonymous function that contains the code you want to execute when the page is loaded.
- `alert("Page loaded!");`: This is an example of code that is executed when the page is loaded.

## Helpful links

- [jQuery Documentation - $(document).ready()](https://api.jquery.com/ready/)

onelinerhub: [load

How do I use jQuery onload?](https://onelinerhub.com/jquery/load--how-do-i-use-jquery-onload)