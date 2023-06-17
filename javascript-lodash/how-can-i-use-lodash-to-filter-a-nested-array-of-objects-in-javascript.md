# How can I use Lodash to filter a nested array of objects in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to filter a nested array of objects in JavaScript.

Here is an example of how to use Lodash to filter a nested array of objects:

```
const data = [
  {
    id: 1,
    name: 'John',
    age: 20
  },
  {
    id: 2,
    name: 'Jill',
    age: 30
  },
  {
    id: 3,
    name: 'Jack',
    age: 25
  }
]

const result = _.filter(data, { age: 25 });

console.log(result);
```
## Output example

```
[
  {
    id: 3,
    name: 'Jack',
    age: 25
  }
]
```

The code above uses Lodash's `_.filter()` function to filter the `data` array. It takes two arguments: the array to be filtered, and an object containing the filter criteria. In this case, the filter criteria is `{ age: 25 }`, which will filter the array to only include objects with an `age` of `25`. The result is stored in the `result` variable, which is then logged to the console.

- `_.filter()`: [https://lodash.com/docs/4.17.15#filter](https://lodash.com/docs/4.17.15#filter)
- `data`: The array of objects to be filtered
- `{ age: 25 }`: The filter criteria object
- `result`: The filtered array of objects containing only objects with an `age` of `25`

onelinerhub: [How can I use Lodash to filter a nested array of objects in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-filter-a-nested-array-of-objects-in-javascript)