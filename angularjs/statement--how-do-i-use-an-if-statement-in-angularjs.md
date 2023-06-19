# statement

How do I use an if statement in AngularJS?
// plain

An `if` statement in AngularJS is used to conditionally execute a set of code depending on a given condition. In order to use an `if` statement, you will need to use the `ng-if` directive. This directive will evaluate an expression and if the expression evaluates to true, the element and its children will be displayed.

## Example code

```
<p ng-if="user.age > 18">You are an adult</p>
```

This example code will check if the user's age is greater than 18. If it is, the text "You are an adult" will be displayed.

## Code explanation


* `ng-if` - The directive used to conditionally display an element.
* `user.age` - The expression that will be evaluated.
* `> 18` - The condition for the expression to evaluate to true.

For more information on using `if` statements in AngularJS, please see the following links:

* [AngularJS ngIf Directive](https://www.w3schools.com/angular/ng_ng-if.asp)
* [AngularJS ngIf Documentation](https://docs.angularjs.org/api/ng/directive/ngIf)

onelinerhub: [statement

How do I use an if statement in AngularJS?](https://onelinerhub.com/angularjs/statement--how-do-i-use-an-if-statement-in-angularjs)