# How do I use a backbone.js comparator to compare two values?
// plain

A comparator is a function in Backbone.js that allows you to compare two values. To use a comparator, you need to define a function that takes two parameters and returns either a negative value, a positive value, or 0 if the two values are equal. For example:

```
function compareValues(a, b) {
  if (a < b) {
    return -1;
  } else if (a > b) {
    return 1;
  } else {
    return 0;
  }
}
```

The `compareValues` function takes two parameters, `a` and `b`, and compares them. If `a` is less than `b`, the function returns a negative value. If `a` is greater than `b`, the function returns a positive value. If `a` is equal to `b`, the function returns 0.

Once the comparator is defined, you can use it in Backbone.js to compare two values. For example:

```
var val1 = 5;
var val2 = 10;

var comparison = compareValues(val1, val2);
console.log(comparison); // Output: -1
```

In the above example, the `compareValues` function is used to compare `val1` and `val2`. Since `val1` is less than `val2`, the function returns -1.

The following are the parts of the code and their explanations:

- `function compareValues(a, b)`: This is the function definition for the comparator. It takes two parameters, `a` and `b`, and compares them.

- `if (a < b) {`: This is an `if` statement that checks if `a` is less than `b`. If it is, the code inside the `if` block is executed.

- `return -1;`: This is the return statement that returns -1 if `a` is less than `b`.

- `else if (a > b) {`: This is an `else if` statement that checks if `a` is greater than `b`. If it is, the code inside the `else if` block is executed.

- `return 1;`: This is the return statement that returns 1 if `a` is greater than `b`.

- `else {`: This is an `else` statement that is executed if `a` is equal to `b`.

- `return 0;`: This is the return statement that returns 0 if `a` is equal to `b`.

- `var comparison = compareValues(val1, val2);`: This is the line of code that calls the `compareValues` function and stores the result in the `comparison` variable.

- `console.log(comparison);`: This is the line of code that prints the value of the `comparison` variable to the console.

## Helpful links
- [Backbone.js Comparator Documentation](http://backbonejs.org/#Comparator)

onelinerhub: [How do I use a backbone.js comparator to compare two values?](https://onelinerhub.com/backbone.js/how-do-i-use-a-backbone-js-comparator-to-compare-two-values)