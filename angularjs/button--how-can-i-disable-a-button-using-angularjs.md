# button

How can I disable a button using AngularJS?
// plain

To disable a button using AngularJS, the `ng-disabled` directive can be used. This directive binds the enabled/disabled state of a form control (such as a button) to an expression. If the expression evaluates to `true`, then the element is disabled.

For example, the following code will disable a button when the `isDisabled` variable is `true`:

```html
<button ng-disabled="isDisabled">Click Me</button>
```

The `isDisabled` variable can be set in the controller:

```javascript
$scope.isDisabled = true;
```

## Code explanation


- `ng-disabled`: This directive binds the enabled/disabled state of a form control (such as a button) to an expression. If the expression evaluates to `true`, then the element is disabled.
- `isDisabled`: This is a variable that is set in the controller. It is used to determine whether the button should be enabled or disabled.

## Helpful links

- [AngularJS ng-disabled Directive](https://www.w3schools.com/angular/ng_ng-disabled.asp)

onelinerhub: [button

How can I disable a button using AngularJS?](https://onelinerhub.com/angularjs/button--how-can-i-disable-a-button-using-angularjs)