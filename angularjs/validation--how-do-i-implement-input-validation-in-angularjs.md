# validation

How do I implement input validation in AngularJS?
// plain

Input validation in AngularJS is a process of ensuring that user input is in the correct format and within the expected boundaries. It helps to prevent malicious data from being entered into the system.

## Example code


```
// Define a custom validator
angular.module('myApp', [])
.directive('validateNumber', function() {
  return {
    require: 'ngModel',
    link: function(scope, element, attrs, ctrl) {
      ctrl.$validators.number = function(modelValue, viewValue) {
        if (ctrl.$isEmpty(modelValue)) {
          // consider empty models to be valid
          return true;
        }
        if (NUMBER_REGEXP.test(viewValue)) {
          // it is valid
          return true;
        }
        // it is invalid
        return false;
      };
    }
  };
});
```

In the above example, a custom validator is defined for a number input field. The validator runs a regular expression against the input to check if the value is a valid number. If it is not a valid number, the validator will return false.

Parts of the code:
- `angular.module('myApp', [])`: This line defines the AngularJS module.
- `.directive('validateNumber', function() {`: This line defines a custom directive for validating a number field.
- `ctrl.$validators.number = function(modelValue, viewValue) {`: This line defines a validator function that will be called when the input is changed.
- `if (NUMBER_REGEXP.test(viewValue)) {`: This line tests the input against a regular expression to check if it is a valid number.

## Helpful links
- [AngularJS Form Validation](https://docs.angularjs.org/guide/forms)
- [AngularJS Directive Documentation](https://docs.angularjs.org/api/ng/directive)

onelinerhub: [validation

How do I implement input validation in AngularJS?](https://onelinerhub.com/angularjs/validation--how-do-i-implement-input-validation-in-angularjs)