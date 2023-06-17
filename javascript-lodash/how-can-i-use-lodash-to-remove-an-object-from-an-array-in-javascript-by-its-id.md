# How can I use Lodash to remove an object from an array in JavaScript by its ID?
// plain

Using Lodash, you can remove an object from an array in JavaScript by its ID with the `_.remove()` method. This method accepts two parameters: an array and a function. The function should return a boolean value; true if the item should be removed, and false otherwise.

For example:

```
const array = [
  { id: 1, name: 'One' },
  { id: 2, name: 'Two' },
  { id: 3, name: 'Three' },
];

_.remove(array, item => item.id === 2);
console.log(array);
```

## Output example


```
[
  { id: 1, name: 'One' },
  { id: 3, name: 'Three' },
]
```

The code above uses the `_.remove()` method to remove an object from the `array` with the `id` of `2`. The `_.remove()` method iterates through the array and passes each item to the function. If the function returns `true`, the item is removed from the array.

## Code explanation

- `const array = [` - declares a constant named `array` and assigns it to an array of objects
- `{ id: 1, name: 'One' },` - an object in the array with an `id` of `1` and a `name` of `One`
- `{ id: 2, name: 'Two' },` - an object in the array with an `id` of `2` and a `name` of `Two`
- `{ id: 3, name: 'Three' },` - an object in the array with an `id` of `3` and a `name` of `Three`
- `_.remove(array, item => item.id === 2);` - calls the `_.remove()` method with the `array` and a function that returns `true` if the `item`'s `id` is `2`
- `console.log(array);` - logs the modified array to the console

## Helpful links
- [Lodash Documentation - _.remove()](https://lodash.com/docs/4.17.15#remove)

onelinerhub: [How can I use Lodash to remove an object from an array in JavaScript by its ID?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-remove-an-object-from-an-array-in-javascript-by-its-id)