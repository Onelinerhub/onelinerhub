# validation

How do I use AngularJS to validate a form?
// plain

AngularJS provides a powerful tool for form validation. It can be used to validate user input before submission. To use AngularJS for form validation, you need to include the `ng-model` directive in your form elements. This directive binds the user input to the model, and allows you to check the validity of the input.

You can use the `$valid` and `$invalid` properties to check if the form is valid or not.

## Example code


```
<form name="myForm">
  <input type="text" ng-model="name" required>
  <button ng-disabled="myForm.$invalid">Submit</button>
</form>
```

This code will disable the submit button if the form is invalid.

## Code explanation


- `ng-model` directive: binds user input to the model
- `$valid` and `$invalid` properties: check if the form is valid or not
- `ng-disabled` directive: used to disable the submit button if the form is invalid

## Helpful links

- [AngularJS Form Validation](https://docs.angularjs.org/guide/forms)
- [Form Validation in AngularJS](https://www.tutorialspoint.com/angularjs/angularjs_form_validation.htm)

onelinerhub: [validation

How do I use AngularJS to validate a form?](https://onelinerhub.com/angularjs/validation--how-do-i-use-angularjs-to-validate-a-form)