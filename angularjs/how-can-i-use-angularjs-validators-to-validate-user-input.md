# How can I use AngularJS validators to validate user input?
// plain

AngularJS provides a set of built-in validators that can be used to validate user input. The validators are used in the form of directives, and they can be used to validate text, numbers, and dates.

For example, the `ng-minlength` directive can be used to validate the minimum length of a text input field:

```
<input type="text" ng-minlength="5" />
```

If a user attempts to submit a value that is shorter than 5 characters, the form will be invalid.

The `ng-pattern` directive can be used to validate the format of a text input field:

```
<input type="text" ng-pattern="/^[a-zA-Z]+$/" />
```

This directive will only allow letters (no numbers or special characters) to be submitted.

The `ng-max` directive can be used to validate the maximum value of a number input field:

```
<input type="number" ng-max="100" />
```

If a user attempts to submit a value that is greater than 100, the form will be invalid.

The `ng-min` directive can be used to validate the minimum value of a date input field:

```
<input type="date" ng-min="01/01/2000" />
```

If a user attempts to submit a date that is before 01/01/2000, the form will be invalid.

These are just a few of the validators available in AngularJS. For more information, please see the [AngularJS Documentation](https://docs.angularjs.org/guide/forms).

onelinerhub: [How can I use AngularJS validators to validate user input?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-validators-to-validate-user-input)