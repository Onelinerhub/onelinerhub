# How do I create an AngularJS service?
// plain

An AngularJS service is a singleton object created by a service factory. Services are the most common type of AngularJS dependency injection and are used to share data and functionality across the application.

To create an AngularJS service, start by creating a service factory function. This function will return the singleton object that represents the service.

```javascript
// Create the myService service
angular.module('myApp').factory('myService', function() {
  var service = {
    // service properties and methods go here
  };
  return service;
});
```

The service factory function can accept additional parameters that will be injected into the function when it is invoked by AngularJS. These parameters can be used to inject other services or values into the service.

```javascript
// Create the myService service
angular.module('myApp').factory('myService', function(someOtherService) {
  var service = {
    // service properties and methods go here
  };
  return service;
});
```

The service factory function can also contain properties and methods that will be available on the singleton object that is returned.

```javascript
// Create the myService service
angular.module('myApp').factory('myService', function() {
  var service = {
    someProperty: 'someValue',
    someMethod: function() {
      // do something
    }
  };
  return service;
});
```

Once the service factory function is defined, it can be injected into any component that needs access to the service.

For more information about creating and using services in AngularJS, see the [AngularJS documentation](https://docs.angularjs.org/guide/services).

onelinerhub: [How do I create an AngularJS service?](https://onelinerhub.com/angularjs/how-do-i-create-an-angularjs-service)