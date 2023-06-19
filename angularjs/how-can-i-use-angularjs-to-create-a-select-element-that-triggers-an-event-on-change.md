# How can I use AngularJS to create a select element that triggers an event on change?
// plain

To create a select element that triggers an event on change using AngularJS, you can use the `ng-change` directive. This directive will evaluate an expression whenever the value of the element changes.

For example, the following code will create a select element with two options, and when the value of the select element is changed, the `onChange()` function will be called:

```html
<select ng-model="selectedOption" ng-change="onChange()">
  <option value="option1">Option 1</option>
  <option value="option2">Option 2</option>
</select>
```

The `onChange()` function can be defined in the controller, and will be called whenever the select element is changed.

```js
$scope.onChange = function() {
  console.log('Value changed to', $scope.selectedOption);
};
```

The output of the above code will be:
```
Value changed to option1
```

## Code explanation

- `ng-change` directive - this directive will evaluate an expression whenever the value of the element changes.
- `ng-model` directive - this directive binds the value of the element to a property on the scope.
- `onChange()` function - this function is called whenever the value of the select element is changed.

## Helpful links
- [ngChange](https://docs.angularjs.org/api/ng/directive/ngChange)
- [ngModel](https://docs.angularjs.org/api/ng/directive/ngModel)

onelinerhub: [How can I use AngularJS to create a select element that triggers an event on change?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-create-a-select-element-that-triggers-an-event-on-change)