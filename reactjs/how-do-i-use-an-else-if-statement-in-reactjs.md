# How do I use an else if statement in ReactJS?
// plain

An `else if` statement is a conditional statement that allows you to check for multiple conditions in ReactJS. It is used when you want to check for more than one condition.

## Example code

```
function myFunc(num) {
  if (num > 10) {
    return "Number is greater than 10";
  } else if (num < 10) {
    return "Number is less than 10";
  } else {
    return "Number is equal to 10";
  }
}
```
## Output example

```
Number is equal to 10
```

The code above checks for three conditions: if the number is greater than 10, if the number is less than 10, and if the number is equal to 10. If the number is greater than 10, it returns "Number is greater than 10". If the number is less than 10, it returns "Number is less than 10". If the number is equal to 10, it returns "Number is equal to 10".

## Code explanation

- `function myFunc(num)`: This is the function that will contain the `else if` statement. The parameter `num` is the number that will be checked.
- `if (num > 10)`: This is the first condition that will be checked. If the number is greater than 10, the code inside the `if` statement will be executed.
- `else if (num < 10)`: This is the second condition that will be checked. If the number is less than 10, the code inside the `else if` statement will be executed.
- `else`: This is the third condition that will be checked. If the number is equal to 10, the code inside the `else` statement will be executed.

## Helpful links
- [React Docs - Conditional Rendering](https://reactjs.org/docs/conditional-rendering.html)
- [MDN - if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)

onelinerhub: [How do I use an else if statement in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-an-else-if-statement-in-reactjs)