# How do I use Lodash to remove an element from an array in JavaScript?
// plain

Using Lodash, you can easily remove an element from an array in JavaScript. The _.pull() method is the most efficient way to do this. It takes two arguments, the array you want to modify and the element you want to remove.

## Example code

```
const array = [1, 2, 3, 4, 5, 6];

_.pull(array, 2);

console.log(array);
```
## Output example

```
[1, 3, 4, 5, 6]
```

The code above will remove the element 2 from the array.

## Code explanation

* `const array = [1, 2, 3, 4, 5, 6];` - declaring a variable and assigning an array to it
* `_.pull(array, 2);` - calling the Lodash _.pull() method and passing in the array and the element to remove
* `console.log(array);` - logging the array to the console

## Helpful links
* [Lodash Documentation - _.pull()](https://lodash.com/docs/4.17.15#pull)

onelinerhub: [How do I use Lodash to remove an element from an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-remove-an-element-from-an-array-in-javascript)