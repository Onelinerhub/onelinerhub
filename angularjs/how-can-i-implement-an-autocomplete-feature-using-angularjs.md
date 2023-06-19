# How can I implement an autocomplete feature using AngularJS?
// plain

An autocomplete feature can be implemented using AngularJS by using the `ng-model` and `ng-options` directives. The `ng-model` directive binds the user input to a variable, while the `ng-options` directive binds the list of possible values to the `ng-model` variable.

For example, the following code creates an autocomplete feature for selecting a language:

```html
<input type="text" ng-model="language" ng-options="language for language in languages">
```

```js
$scope.languages = [
  'Javascript',
  'Python',
  'Java',
  'C++'
];
```

The `ng-model` directive binds the user input to the `language` variable, while the `ng-options` directive binds the list of possible languages to the `language` variable. When the user types in the input field, the `language` variable is updated with the user input. The list of possible values is filtered based on the user input and the user can select a language from the list.

## Code explanation
**
- `ng-model` directive: binds the user input to a variable
- `ng-options` directive: binds the list of possible values to the `ng-model` variable
- `$scope.languages`: array of language strings

**## Helpful links**
- https://docs.angularjs.org/api/ng/directive/ngModel
- https://docs.angularjs.org/api/ng/directive/ngOptions

onelinerhub: [How can I implement an autocomplete feature using AngularJS?](https://onelinerhub.com/angularjs/how-can-i-implement-an-autocomplete-feature-using-angularjs)