# How do I use an AngularJS variable in a template?
// plain

An AngularJS variable can be used in a template by assigning it to the `$scope` object in the controller. The variable can then be accessed from the template using the `{{}}` syntax.

For example, the following code will assign a variable called `name` to the `$scope` object in the controller and display it in the template:

Controller:
```javascript
$scope.name = 'John';
```

Template:
```html
<p>Hello {{name}}!</p>
```

## Output example

```
Hello John!
```

## Code explanation

- `$scope.name = 'John';` - assigns the string `John` to the variable `name` on the `$scope` object in the controller
- `{{name}}` - accesses the `name` variable from the template

## Helpful links
- [AngularJS Documentation - Scopes](https://docs.angularjs.org/guide/scope)
- [AngularJS Documentation - Expressions](https://docs.angularjs.org/guide/expression)

onelinerhub: [How do I use an AngularJS variable in a template?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-variable-in-a-template)