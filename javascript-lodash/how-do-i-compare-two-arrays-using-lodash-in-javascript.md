# How do I compare two arrays using Lodash in JavaScript?
// plain

Comparing two arrays using Lodash in JavaScript is a straightforward task. To do this, one can use the `_.isEqual()` method. This method will compare two arrays and return `true` if they are equal and `false` if they are not.

For example:

```
let array1 = [1, 2, 3];
let array2 = [1, 2, 3];

let result = _.isEqual(array1, array2);

console.log(result);
```

## Output example

```
true
```

The code above uses the `_.isEqual()` method to compare the two arrays `array1` and `array2`. The `_.isEqual()` method takes two parameters, the two arrays to be compared, and returns `true` if they are equal and `false` if they are not. In this case, the two arrays are equal, so the output is `true`.

The `_.isEqual()` method is just one of many Lodash methods that can be used to compare arrays. Other methods include `_.isMatch()`, `_.difference()`, and `_.xor()`.

## Helpful links

- [Lodash Documentation for _.isEqual()](https://lodash.com/docs/4.17.15#isEqual)
- [Lodash Documentation for _.isMatch()](https://lodash.com/docs/4.17.15#isMatch)
- [Lodash Documentation for _.difference()](https://lodash.com/docs/4.17.15#difference)
- [Lodash Documentation for _.xor()](https://lodash.com/docs/4.17.15#xor)

onelinerhub: [How do I compare two arrays using Lodash in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-compare-two-arrays-using-lodash-in-javascript)