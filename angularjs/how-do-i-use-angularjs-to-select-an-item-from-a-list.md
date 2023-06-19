# How do I use AngularJS to select an item from a list?
// plain

To select an item from a list in AngularJS, you can use the `ng-model` directive. This directive binds the value of the form element to a property of the scope. In the example below, the `selectedItem` property of the scope is bound to the `<select>` element.

```html
<select ng-model="selectedItem">
  <option value="item1">Item 1</option>
  <option value="item2">Item 2</option>
  <option value="item3">Item 3</option>
</select>
```

The `selectedItem` property of the scope can then be accessed in the controller.

```js
app.controller('MyCtrl', function($scope) {
  console.log($scope.selectedItem);
});
```

The output of the example code above is the value of the item selected in the `<select>` element.

## Code explanation

* `ng-model` directive - binds the value of the form element to a property of the scope
* `<select>` element - contains the list of items
* `selectedItem` property of the scope - contains the value of the item selected in the `<select>` element
* `console.log()` - prints the value of the `selectedItem` property of the scope

## Helpful links
* [AngularJS ng-model Directive](https://www.w3schools.com/angular/ng_ng-model.asp)

onelinerhub: [How do I use AngularJS to select an item from a list?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-select-an-item-from-a-list)