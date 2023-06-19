# How can I use the "track by" feature in AngularJS?
// plain

The "track by" feature in AngularJS allows you to specify a custom identifier to associate each item in a collection with a unique identifier. This feature is especially useful when working with large collections of data, as it allows you to quickly and easily identify which items have been added or removed from the collection.

For example, the following code block will create an array of objects and use the "track by" feature to associate each object with its unique id:

```javascript
var myArray = [
  {id: 1, name: 'John'},
  {id: 2, name: 'Jane'}
];

$scope.myArray = myArray;
$scope.trackByFn = function(item) {
  return item.id;
};
```

In the HTML template, you can use the `track by` expression to specify the custom identifier to use for the collection:

```html
<div ng-repeat="item in myArray track by trackByFn(item)">
  {{ item.name }}
</div>
```

The `trackByFn` function will be called for each item in the collection, and the value it returns will be used as the unique identifier for that item. This allows Angular to quickly and easily identify which items have been added or removed from the collection.

## Code explanation


1. `var myArray = [{id: 1, name: 'John'}, {id: 2, name: 'Jane'}];`: This creates an array of objects, with each object containing an `id` and a `name` property.

2. `$scope.myArray = myArray;`: This assigns the array of objects to a scope variable, making it available to the HTML template.

3. `$scope.trackByFn = function(item) { return item.id; };`: This creates a function that takes an item as an argument and returns the `id` property of that item.

4. `<div ng-repeat="item in myArray track by trackByFn(item)">`: This uses the `track by` expression to specify the `trackByFn` function as the custom identifier for the collection.

Here are some relevant links for further reading:

- [AngularJS Documentation on track by](https://docs.angularjs.org/api/ng/directive/ngRepeat#tracking-and-duplicates)
- [Tutorial on track by](https://www.codementor.io/angularjs/tutorial/angularjs-track-by-example)

onelinerhub: [How can I use the "track by" feature in AngularJS?](https://onelinerhub.com/angularjs/how-can-i-use-the--track-by--feature-in-angularjs)