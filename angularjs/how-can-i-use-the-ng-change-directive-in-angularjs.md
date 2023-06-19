# How can I use the ng-change directive in AngularJS?
// plain

The `ng-change` directive in AngularJS allows you to specify custom behavior when an element's value changes. It can be used to respond to user input, validate form fields, or perform calculations.

For example, if you wanted to calculate the total cost of a shopping cart, you could use the `ng-change` directive to update the total when the user changes the quantity of an item:

```html
<input type="number" ng-model="quantity" ng-change="updateTotal()">
<p>Total cost: {{total}}</p>
```

```javascript
$scope.total = 0;
$scope.updateTotal = function() {
  $scope.total = $scope.quantity * 10;
};
```

In the above example, the `updateTotal()` function is called when the user changes the value of the `quantity` input. The function then updates the `total` variable, which is displayed to the user.

Here is a list of parts used in the example:

- `ng-change`: directive used to specify custom behavior when an element's value changes
- `ng-model`: directive used to bind an element's value to a variable in the scope
- `input type="number"`: HTML input element used to accept numeric values
- `updateTotal()`: function used to update the total cost of the shopping cart
- `$scope.total`: variable used to store the total cost of the shopping cart

Here are some ## Helpful links

- [ng-change documentation](https://docs.angularjs.org/api/ng/directive/ngChange)
- [ng-model documentation](https://docs.angularjs.org/api/ng/directive/ngModel)
- [HTML input element documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)

onelinerhub: [How can I use the ng-change directive in AngularJS?](https://onelinerhub.com/angularjs/how-can-i-use-the-ng-change-directive-in-angularjs)