# How do I create and access a global variable in AngularJS?
// plain

Creating and accessing global variables in AngularJS is pretty straightforward. To create a global variable, you just need to create a variable inside the `$rootScope` object. For example:

```
$rootScope.myGlobalVariable = 'Hello World';
```

To access the global variable, you can use `$rootScope.myGlobalVariable` in any controller, directive, or service.

## Code explanation


- `$rootScope`: The `$rootScope` is the parent scope of all other scopes in AngularJS. It is the highest level scope and can be accessed from any other scope.
- `myGlobalVariable`: This is the name of the global variable.
- `'Hello World'`: This is the value of the global variable.

## Helpful links

- [AngularJS Documentation](https://docs.angularjs.org/api/ng/type/$rootScope.Scope)
- [Global Variables in AngularJS](https://www.codementor.io/angularjs/tutorial/global-variables-in-angularjs)

onelinerhub: [How do I create and access a global variable in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-create-and-access-a-global-variable-in-angularjs)