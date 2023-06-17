# How can I use jQuery to hide and show elements?
// plain

jQuery can be used to hide and show elements on a web page. It has a `.hide()` and `.show()` method that can be used to achieve this.

## Example code

```
$(document).ready(function() {
    $("button").click(function(){
        $("#div1").hide();
        $("#div2").show();
    });
});
```

The code above will hide an element with the id `div1` and show an element with the id `div2` when the button is clicked.

The code consists of the following parts:

1. `$(document).ready(function()`: This part of the code ensures that the code runs only after the page has finished loading.
2. `$("button").click(function()`: This part of the code defines the action that will be executed when the button is clicked.
3. `$("#div1").hide()`: This part of the code hides the element with the id `div1`.
4. `$("#div2").show()`: This part of the code shows the element with the id `div2`.

For more information, please refer to the following links:

- [jQuery hide()](https://api.jquery.com/hide/)
- [jQuery show()](https://api.jquery.com/show/)

onelinerhub: [How can I use jQuery to hide and show elements?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-hide-and-show-elements)