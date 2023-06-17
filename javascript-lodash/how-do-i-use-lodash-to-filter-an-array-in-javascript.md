# How do I use Lodash to filter an array in JavaScript?
// plain

Using Lodash to filter an array in JavaScript is simple and straightforward.

The `_.filter()` method is used to filter an array based on a given callback function. The callback function should return `true` for the elements that should be included in the filtered array.

For example:

```javascript
const numbers = [1, 2, 3, 4, 5];

const evenNumbers = _.filter(numbers, (num) => num % 2 === 0);

console.log(evenNumbers);
```

## Output example

```
[2, 4]
```

The code above filters the `numbers` array and returns a new array `evenNumbers` containing only the even numbers.

The `_.filter()` method takes two parameters:
- an array to filter
- a callback function to determine which elements should be included in the filtered array

For more information and examples, see the [Lodash Documentation](https://lodash.com/docs/4.17.15#filter).

onelinerhub: [How do I use Lodash to filter an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-filter-an-array-in-javascript)