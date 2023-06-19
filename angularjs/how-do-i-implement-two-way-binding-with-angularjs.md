# How do I implement two-way binding with AngularJS?
// plain

Two-way binding in AngularJS is the synchronization of data between the view and the model. It allows to update the view when the model changes, as well as update the model when the view changes.

To implement two-way binding in AngularJS, you can use the `ng-model` directive. This directive binds the value of HTML controls (input, select, textarea) to the application data.

For example, if you have a textbox with the `ng-model` directive:
```
<input type="text" ng-model="name">
```

Then, when you type something in the textbox, the `name` variable in the controller is updated automatically.

The following code snippet shows an example of two-way binding in an AngularJS application:
```
<div ng-controller="MyCtrl">
    <input type="text" ng-model="name">
    <p>Hello {{name}}!</p>
</div>

<script>
function MyCtrl($scope) {
    $scope.name = 'World';
}
</script>
```

The output of this code is:
```
Hello World!
```

When you type something in the text box, the output changes accordingly.

For more information, see the [AngularJS documentation](https://docs.angularjs.org/guide/databinding).

onelinerhub: [How do I implement two-way binding with AngularJS?](https://onelinerhub.com/angularjs/how-do-i-implement-two-way-binding-with-angularjs)