# debugging

How can I debug errors in AngularJS?
// plain

Debugging errors in AngularJS can be done in several ways. Firstly, the `$log` service can be used to log messages and errors to the console. The following code block shows an example of how to use `$log` to log an error message:

```
$log.error('Something went wrong!');
```

## Output example

```
Error: Something went wrong!
```

Secondly, the `$exceptionHandler` service can be used to catch and log exceptions. The following code block shows an example of how to use `$exceptionHandler` to log an error message:

```
try {
  // Some code
} catch (e) {
  $exceptionHandler(e);
}
```

## Output example

```
Error: Some error message
```

Thirdly, the `$compile` service can be used to debug and inspect the compilation process of an AngularJS application. The following code block shows an example of how to use `$compile` to inspect an element:

```
var element = $compile('<div>Hello World!</div>')($scope);
```

## Output example

```
<div class="ng-scope">Hello World!</div>
```

Finally, the `$scope` service can be used to debug and inspect the scope of an AngularJS application. The following code block shows an example of how to use `$scope` to inspect the scope of an element:

```
$scope.$watch('someProperty', function (newValue, oldValue) {
  console.log(newValue, oldValue);
});
```

## Output example

```
10 5
```

In summary, debugging errors in AngularJS can be done using the `$log` service to log messages and errors, the `$exceptionHandler` service to catch and log exceptions, the `$compile` service to debug and inspect the compilation process, and the `$scope` service to debug and inspect the scope of an application.

## Helpful links

- [AngularJS Developer Guide - $log](https://docs.angularjs.org/api/ng/service/$log)
- [AngularJS Developer Guide - $exceptionHandler](https://docs.angularjs.org/api/ng/service/$exceptionHandler)
- [AngularJS Developer Guide - $compile](https://docs.angularjs.org/api/ng/service/$compile)
- [AngularJS Developer Guide - $scope](https://docs.angularjs.org/api/ng/type/$rootScope.Scope)

onelinerhub: [debugging

How can I debug errors in AngularJS?](https://onelinerhub.com/angularjs/debugging--how-can-i-debug-errors-in-angularjs)