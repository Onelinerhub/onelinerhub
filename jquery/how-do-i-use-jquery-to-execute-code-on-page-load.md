# How do I use jQuery to execute code on page load?
// plain

Using jQuery to execute code on page load is quite simple. Here is an example code block that will alert a message when the page loads:

```
$(document).ready(function(){
    alert("Page has loaded");
});
```
This will output a message saying "Page has loaded" when the page loads.

The code is composed of the following parts:

* `$(document)` - This is a jQuery selector that selects the document object.
* `.ready()` - This is a jQuery method that is called when the page is finished loading.
* `function(){...}` - This is a JavaScript function that contains the code to be executed when the page is finished loading.
* `alert("Page has loaded")` - This is the code that is executed when the page is finished loading.

## Helpful links
* [jQuery Documentation](https://api.jquery.com/)
* [jQuery `.ready()` Documentation](https://api.jquery.com/ready/)

onelinerhub: [How do I use jQuery to execute code on page load?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-execute-code-on-page-load)