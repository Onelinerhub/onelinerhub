# How can I use Lodash to manipulate HTML elements in JavaScript?
// plain

Lodash is a JavaScript library that provides a lot of useful functions for manipulating HTML elements in JavaScript.

For example, you can use Lodash's `_.map()` function to iterate over an array of elements and modify them. The following code block shows an example of using `_.map()` to add a class to all HTML elements in an array:

```
let elements = [
  "<div>Element 1</div>",
  "<div>Element 2</div>",
  "<div>Element 3</div>"
];

let modifiedElements = _.map(elements, function(element) {
  return element.replace('<div>', '<div class="example-class">');
});

console.log(modifiedElements);
```

## Output example

```
[
  "<div class="example-class">Element 1</div>",
  "<div class="example-class">Element 2</div>",
  "<div class="example-class">Element 3</div>"
]
```

The code above does the following:

1. Declares an array of HTML elements
2. Uses Lodash's `_.map()` function to iterate over the array
3. Inside the `_.map()` function, the `element` parameter is used to access each element in the array
4. The `element.replace()` function is used to add the `example-class` class to each HTML element
5. The resulting modified elements are stored in the `modifiedElements` variable

For more information on using Lodash to manipulate HTML elements in JavaScript, see the following links:

- [Lodash Documentation](https://lodash.com/docs/)
- [Using Lodash to Manipulate HTML Elements](https://www.freecodecamp.org/news/using-lodash-to-manipulate-html-elements-in-javascript-8e13c9f2ec6d/)

onelinerhub: [How can I use Lodash to manipulate HTML elements in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-manipulate-html-elements-in-javascript)