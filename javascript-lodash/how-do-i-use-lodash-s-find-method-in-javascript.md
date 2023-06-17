# How do I use Lodash's find method in JavaScript?
// plain

The `_.find()` method in Lodash is used to search for a value in an array that satisfies a given condition. It returns the first item that satisfies the condition.

## Example code

```
const array = [
  { name: 'John', age: 25 },
  { name: 'Alice', age: 30 },
  { name: 'Bob', age: 25 }
];

const result = _.find(array, { age: 25 });

console.log(result);
```

## Output example

```
{ name: 'John', age: 25 }
```

The code above uses the `_.find()` method to search the array for an item with an `age` property of 25. The `_.find()` method takes two arguments, the array and an object which specifies the condition. In this case, the condition is to find an item with an `age` property of 25. The `_.find()` method returns the first item that satisfies the condition, which in this case is the object `{ name: 'John', age: 25 }`.

## Code explanation


- `const array = [ ... ]`: This declares an array of objects.
- `const result = _.find(array, { age: 25 })`: This uses the `_.find()` method to search the array for an item with an `age` property of 25.
- `console.log(result)`: This prints the result of the `_.find()` method to the console.

For more information on the `_.find()` method, please refer to the [Lodash documentation](https://lodash.com/docs/4.17.15#find).

onelinerhub: [How do I use Lodash's find method in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-s-find-method-in-javascript)