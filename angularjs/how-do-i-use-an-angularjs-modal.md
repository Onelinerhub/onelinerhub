# How do I use an AngularJS modal?
// plain

To use an AngularJS modal, first you need to add the relevant dependencies to your project. This includes the AngularJS library, the Angular-UI Bootstrap library, and the Bootstrap CSS library.

Next, you need to create the HTML template for the modal. This template should include the modal's title, body, and footer.

```html
<div class="modal-header">
    <h3 class="modal-title">My Modal</h3>
</div>
<div class="modal-body">
    <p>This is the content of my modal</p>
</div>
<div class="modal-footer">
    <button class="btn btn-primary" ng-click="ok()">OK</button>
    <button class="btn btn-warning" ng-click="cancel()">Cancel</button>
</div>
```

Then, you need to create the controller for the modal. This controller should include the functions for opening and closing the modal, as well as the logic for the OK and Cancel buttons.

```javascript
angular.module('myApp')
  .controller('MyModalController', function($scope, $uibModalInstance) {
    $scope.ok = function () {
      $uibModalInstance.close();
    };

    $scope.cancel = function () {
      $uibModalInstance.dismiss('cancel');
    };
  });
```

Finally, you need to open the modal in your application. This can be done by injecting the $uibModal service into your controller and calling the open() method.

```javascript
angular.module('myApp')
  .controller('MyController', function($scope, $uibModal) {
    $scope.openModal = function () {
      var modalInstance = $uibModal.open({
        templateUrl: 'myModal.html',
        controller: 'MyModalController'
      });
    };
  });
```

This will open the modal, and the user can click the OK or Cancel buttons to close it.

## Helpful links
- [AngularJS](https://angularjs.org/)
- [Angular-UI Bootstrap](https://angular-ui.github.io/bootstrap/)
- [Bootstrap CSS](https://getbootstrap.com/)

onelinerhub: [How do I use an AngularJS modal?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-modal)