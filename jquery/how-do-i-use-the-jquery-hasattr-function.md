# How do I use the jQuery hasattr function?
// plain

The jQuery hasattr function is used to check if an element has a certain attribute. It takes two parameters, the element and the attribute, and returns a boolean value (true or false).

## Example


```
$(document).ready(function(){
  var hasTitle = $("#myDiv").hasattr("title");
  console.log(hasTitle);
});
```
## Output example
 `true`

## Code explanation

- `$(document).ready(function(){`: This is the jQuery document ready function, which is used to ensure that the code is executed only after the page has finished loading.
- `var hasTitle = $("#myDiv").hasattr("title");`: This is the hasattr function call, which takes two parameters - the element (in this case, the element with the ID of "myDiv") and the attribute ("title").
- `console.log(hasTitle);`: This line prints out the value returned by the hasattr function. In this case, it will be either true or false, depending on whether or not the element has the specified attribute.

## Helpful links
- [jQuery hasattr() Documentation](https://api.jquery.com/hasattr/)

onelinerhub: [How do I use the jQuery hasattr function?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-hasattr-function)