# How do I use the jQuery each function?
// plain

The jQuery `each()` function is used to iterate over a jQuery object, executing a function for each matched element. It is similar to `forEach()` in JavaScript.

Below is an example of the `each()` function:
```
$("p").each(function() {
  console.log($(this).text());
});
```
The output of the code above would be the text of each `<p>` element in the DOM.

The `each()` function takes two arguments:
1. The first argument is a function that is executed for each element in the jQuery object. It takes two arguments: the index of the current element in the list and the element itself.
2. The second argument is an optional argument that is used to set the `this` context within the function.

Here is a more detailed example of the `each()` function:
```
$("li").each(function(index, element) {
  console.log("The index is: " + index + " and the element is: " + element);
});
```
The output of the code above would be the index and the element of each `<li>` element in the DOM.

For more information on the `each()` function, please refer to the [jQuery documentation](https://api.jquery.com/each/).

onelinerhub: [How do I use the jQuery each function?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-each-function)