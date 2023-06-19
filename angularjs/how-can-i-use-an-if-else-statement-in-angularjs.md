# How can I use an if else statement in AngularJS?
// plain

An if else statement in AngularJS is used to execute a set of statements based on a condition. The syntax of the if else statement is as follows:

```
if (condition) {
    // execute this code if condition is true
} else {
    // execute this code if condition is false
}
```

For example, the following code block checks if the number entered by the user is greater than 10. If it is, the code prints "Number is greater than 10", otherwise it prints "Number is not greater than 10".

```
let number = prompt("Enter a number");
if (number > 10) {
    console.log("Number is greater than 10");
} else {
    console.log("Number is not greater than 10");
}
```

## Output example


```
Enter a number: 5
Number is not greater than 10
```

## Code explanation


- `let number = prompt("Enter a number");` - This statement prompts the user to enter a number.

- `if (number > 10) {` - This is the condition that is checked. If the number entered by the user is greater than 10, the code inside the if block will be executed.

- `console.log("Number is greater than 10");` - This statement will be executed if the condition is true.

- `else {` - This statement will be executed if the condition is false.

- `console.log("Number is not greater than 10");` - This statement will be executed if the condition is false.

## Helpful links

- [AngularJS if else statement](https://www.tutorialsteacher.com/angularjs/angularjs-if-else)
- [AngularJS conditionals](https://www.w3schools.com/angular/angular_conditional.asp)

onelinerhub: [How can I use an if else statement in AngularJS?](https://onelinerhub.com/angularjs/how-can-i-use-an-if-else-statement-in-angularjs)