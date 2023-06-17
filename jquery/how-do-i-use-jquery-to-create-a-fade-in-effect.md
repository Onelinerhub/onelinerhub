# How do I use jQuery to create a fade-in effect?
// plain

To create a fade-in effect using jQuery, you can use the `fadeIn()` method. This method is used to gradually increase the opacity of an element from 0 to 1 (fully opaque).

## Example code

```
$(document).ready(function(){
  $("#fadeInButton").click(function(){
    $("#fadeInElement").fadeIn();
  });
});
```

This code creates a button with an ID of `fadeInButton` and an element with an ID of `fadeInElement`. When the button is clicked, the `fadeIn()` method is called on the element, gradually increasing its opacity from 0 to 1.

## Code explanation


- `$(document).ready(function(){...});`: This code ensures that the jQuery code will only run once the page has finished loading.

- `$("#fadeInButton").click(function(){...});`: This code creates an event listener for the button with an ID of `fadeInButton`. When the button is clicked, the function inside the brackets will be executed.

- `$("#fadeInElement").fadeIn();`: This code calls the `fadeIn()` method on the element with an ID of `fadeInElement`, gradually increasing its opacity from 0 to 1.

## Helpful links

- [jQuery Documentation - fadeIn()](https://api.jquery.com/fadeIn/)
- [jQuery Documentation - ready()](https://api.jquery.com/ready/)
- [jQuery Documentation - click()](https://api.jquery.com/click/)

onelinerhub: [How do I use jQuery to create a fade-in effect?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-create-a-fade-in-effect)