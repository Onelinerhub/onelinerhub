# How do I use Lodash in a JavaScript playground?
// plain

Lodash is a popular JavaScript library that provides utility functions for common programming tasks. It can be used in a JavaScript playground to quickly prototype code and try out new ideas.

To use Lodash in a JavaScript playground, first you need to include the library. This can be done by adding a `<script>` tag to the HTML of the page, or using a CDN link. For example:

```
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.15/lodash.min.js"></script>
```

Once the library is included, you can start using its functions in your code. For example, the following code uses the `_.map()` function to double each element in an array:

```
const array = [1, 2, 3];
const doubled = _.map(array, (num) => num * 2);
console.log(doubled);
// Output: [2, 4, 6]
```

The code consists of the following parts:

* `const array = [1, 2, 3]`: This creates an array with three elements.
* `const doubled = _.map(array, (num) => num * 2)`: This uses the `_.map()` function from Lodash to double each element in the array.
* `console.log(doubled)`: This prints the resulting array to the console.

For more information on using Lodash in a JavaScript playground, see the [Lodash documentation](https://lodash.com/docs/4.17.15) or the [Lodash API reference](https://lodash.com/docs/4.17.15#map).

onelinerhub: [How do I use Lodash in a JavaScript playground?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-in-a-javascript-playground)