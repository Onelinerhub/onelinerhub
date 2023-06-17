# How can I use the Lodash library in a JavaScript playground?
// plain

The [Lodash](https://lodash.com/) library is a JavaScript utility library that provides many useful functions for manipulating and working with objects, arrays, strings, and numbers. To use Lodash in a JavaScript playground, you can include it in a script tag:

```
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.15/lodash.min.js"></script>
```

Then you can use any of Lodash's functions in your code. For example, to capitalize a string:

```
const str = 'hello world';
const capitalizedStr = _.capitalize(str);
console.log(capitalizedStr);
```

## Output example

```
Hello world
```

The code above uses the `_.capitalize()` function from Lodash to capitalize the string `hello world`. This function is part of the [String methods](https://lodash.com/docs/4.17.15#capitalize) available in the Lodash library.

For more information on using Lodash, see the [Lodash documentation](https://lodash.com/docs/4.17.15/).

onelinerhub: [How can I use the Lodash library in a JavaScript playground?](https://onelinerhub.com/javascript-lodash/how-can-i-use-the-lodash-library-in-a-javascript-playground)