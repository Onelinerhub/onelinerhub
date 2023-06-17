# How can I use jQuery to redirect a user to a different page?
// plain

To use jQuery to redirect a user to a different page, you can use the `window.location` object. This object provides properties and methods for accessing and manipulating the current URL.

## Example code

```
$(document).ready(function(){
    window.location.href = "http://www.example.com";
});
```

The code above will redirect the user to the URL `http://www.example.com` when the document is ready.

The code consists of the following parts:
* `$(document).ready(function(){` - This is a jQuery function that runs the code inside the brackets when the document is ready.
* `window.location.href = "http://www.example.com";` - This sets the `href` property of the `window.location` object to the URL `http://www.example.com`.
* `});` - This closes the `$(document).ready(function(){` function.

## Helpful links
* [jQuery .ready()](https://api.jquery.com/ready/)
* [window.location](https://developer.mozilla.org/en-US/docs/Web/API/Window/location)

onelinerhub: [How can I use jQuery to redirect a user to a different page?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-redirect-a-user-to-a-different-page)