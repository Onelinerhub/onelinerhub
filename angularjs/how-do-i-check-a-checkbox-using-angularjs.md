# How do I check a checkbox using AngularJS?
// plain

To check a checkbox using AngularJS, you can use the `ng-model` directive. This directive binds the value of the checkbox to a variable in the scope of the controller.

For example, below is a simple HTML checkbox with the `ng-model` directive bound to the variable `checkboxModel`:
```html
<input type="checkbox" ng-model="checkboxModel" />
```

To set the checkbox to true, you can set the variable `checkboxModel` to `true` in the controller:
```javascript
$scope.checkboxModel = true;
```

## Code explanation

- `input type="checkbox"`: this is the HTML element for a checkbox
- `ng-model`: this is the AngularJS directive that binds the value of the checkbox to a variable in the scope of the controller
- `$scope.checkboxModel = true`: this is the variable in the controller that sets the checkbox to true

## Helpful links
- [AngularJS ng-model Directive](https://www.w3schools.com/angular/ng_ng-model.asp)

onelinerhub: [How do I check a checkbox using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-check-a-checkbox-using-angularjs)