# How do I use Lodash to compare two objects for deep equality in JavaScript?
// plain

Using Lodash, you can compare two objects for deep equality in JavaScript by using the `_.isEqual()` method. This method compares the values of two objects and returns a boolean value indicating whether the objects are deeply equal.

## Example


```
const object1 = {
  a: {
    b: {
      c: 'foo'
    }
  }
}

const object2 = {
  a: {
    b: {
      c: 'foo'
    }
  }
}

console.log(_.isEqual(object1, object2))
```

## Output example


```
true
```

**Explanation:**

- `const object1` and `const object2`: These two variables define two objects with the same structure and values.
- `_.isEqual()`: This is the Lodash method used to compare two objects for deep equality.
- `object1` and `object2`: These are the two objects being compared.
- `console.log()`: This is used to log the result of the comparison to the console.

**## Helpful links**

- Lodash Documentation: https://lodash.com/docs/4.17.15
- `_.isEqual()`: https://lodash.com/docs/4.17.15#isEqual

onelinerhub: [How do I use Lodash to compare two objects for deep equality in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-compare-two-objects-for-deep-equality-in-javascript)