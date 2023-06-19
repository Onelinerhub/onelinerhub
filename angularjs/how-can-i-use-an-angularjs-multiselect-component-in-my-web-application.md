# How can I use an AngularJS multiselect component in my web application?
// plain

Using an AngularJS multiselect component in a web application is a great way to provide users with multiple selectable options. The following example code shows how to use a multiselect component with AngularJS:

```
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.7/angular.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/angular-ui-select/0.20.0/select.min.js"></script>
  </head>
  <body>
    <div ng-app="myApp" ng-controller="myCtrl">
      <ui-select multiple ng-model="selectedItems" theme="bootstrap" close-on-select="false">
        <ui-select-match placeholder="Select items">{{$item}}</ui-select-match>
        <ui-select-choices repeat="item in items | filter: $select.search">
          {{item}}
        </ui-select-choices>
      </ui-select>
    </div>
    <script>
      var app = angular.module('myApp', ['ui.select']);
      app.controller('myCtrl', function($scope) {
        $scope.items = ["Option 1", "Option 2", "Option 3"];
        $scope.selectedItems = ["Option 1", "Option 3"];
      });
    </script>
  </body>
</html>
```

The code above will create a multiselect component with the options "Option 1", "Option 2", and "Option 3". The selected items will be "Option 1" and "Option 3".

The code consists of the following parts:

- `<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.7/angular.min.js"></script>`: This line includes the AngularJS library.
- `<script src="https://cdnjs.cloudflare.com/ajax/libs/angular-ui-select/0.20.0/select.min.js"></script>`: This line includes the Angular UI Select library, which provides the multiselect component.
- `<div ng-app="myApp" ng-controller="myCtrl">`: This line creates an AngularJS application and controller.
- `<ui-select multiple ng-model="selectedItems" theme="bootstrap" close-on-select="false">`: This line creates the multiselect component. The `multiple` attribute indicates that multiple options can be selected. The `ng-model` attribute binds the component to the `selectedItems` variable in the controller, which stores the selected items. The `theme` attribute sets the component's styling to "bootstrap". The `close-on-select` attribute indicates that the component should not close when an item is selected.
- `<ui-select-match placeholder="Select items">{{$item}}</ui-select-match>`: This line creates the placeholder text for the component.
- `<ui-select-choices repeat="item in items | filter: $select.search">`: This line creates the list of options for the component. The `repeat` attribute indicates that the list of options is stored in the `items` variable in the controller. The `filter` attribute indicates that the list should be filtered based on the user's search input.
- `<script>`: This section of code defines the controller. The `items` variable stores the list of options for the component, and the `selectedItems` variable stores the selected items.

For more information, see the [Angular UI Select documentation](https://github.com/angular-ui/ui-select).

onelinerhub: [How can I use an AngularJS multiselect component in my web application?](https://onelinerhub.com/angularjs/how-can-i-use-an-angularjs-multiselect-component-in-my-web-application)