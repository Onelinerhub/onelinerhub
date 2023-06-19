# How do I use AngularJS lifecycle hooks?
// plain

AngularJS lifecycle hooks are used to tap into the different stages of the AngularJS application's lifecycle. These hooks are exposed as functions that are called at specific points in the lifecycle of a component, directive, or service.

The most commonly used AngularJS lifecycle hooks are:

- `$onInit()`: This hook is called after the controller and its dependencies have been initialized.

## Example code

```
angular.module('myApp', [])
  .controller('myController', function() {
    this.$onInit = function() {
      console.log('Controller initialized!');
    };
  });
```

## Output example

```
Controller initialized!
```

- `$onChanges()`: This hook is called after one-way or two-way bindings have been updated.

## Example code

```
angular.module('myApp', [])
  .controller('myController', function() {
    this.name = 'John';
    this.$onChanges = function(changesObj) {
      console.log('Name changed to ' + changesObj.name.currentValue);
    };
  });
```

## Output example

```
Name changed to John
```

- `$onDestroy()`: This hook is called just before the controller is destroyed.

## Example code

```
angular.module('myApp', [])
  .controller('myController', function() {
    this.$onDestroy = function() {
      console.log('Controller destroyed!');
    };
  });
```

## Output example

```
Controller destroyed!
```

For more information, see the [AngularJS documentation](https://docs.angularjs.org/guide/lifecycle-hooks).

onelinerhub: [How do I use AngularJS lifecycle hooks?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-lifecycle-hooks)