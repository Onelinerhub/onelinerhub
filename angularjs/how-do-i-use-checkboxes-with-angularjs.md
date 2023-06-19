# How do I use checkboxes with AngularJS?
// plain

In order to use checkboxes with AngularJS, you can use the `ng-model` directive. This directive binds the value of the checkbox to a variable in the scope. For example:

```html
<input type="checkbox" ng-model="myCheckbox">
```

This will bind the value of the checkbox to the `myCheckbox` variable in the scope. To set the initial value of the checkbox, you can use the `ng-init` directive. For example:

```html
<input type="checkbox" ng-model="myCheckbox" ng-init="myCheckbox=true">
```

This will set the initial value of the checkbox to `true`.

You can also use the `ng-change` directive to run a function when the value of the checkbox changes. For example:

```html
<input type="checkbox" ng-model="myCheckbox" ng-change="myFunction()">
```

This will run the `myFunction()` function whenever the value of the checkbox changes.

You can also use the `ng-true-value` and `ng-false-value` directives to set the value of the checkbox to a specific value. For example:

```html
<input type="checkbox" ng-model="myCheckbox" ng-true-value="yes" ng-false-value="no">
```

This will set the value of the checkbox to `yes` if it is checked, and `no` if it is not checked.

## Helpful links

- [ng-model Directive](https://docs.angularjs.org/api/ng/directive/ngModel)
- [ng-init Directive](https://docs.angularjs.org/api/ng/directive/ngInit)
- [ng-change Directive](https://docs.angularjs.org/api/ng/directive/ngChange)
- [ng-true-value Directive](https://docs.angularjs.org/api/ng/directive/ngTrueValue)
- [ng-false-value Directive](https://docs.angularjs.org/api/ng/directive/ngFalseValue)

onelinerhub: [How do I use checkboxes with AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-checkboxes-with-angularjs)