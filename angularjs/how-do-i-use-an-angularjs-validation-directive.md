# How do I use an AngularJS validation directive?
// plain

To use an AngularJS validation directive, you need to create an HTML form and add the appropriate AngularJS directives to the HTML elements. The following example shows how to use the `ng-minlength` directive to validate that a text field is at least 5 characters long:

```
<form name="myForm">
  <input type="text" name="myInput" ng-minlength="5" />
</form>
```

The `ng-minlength` directive is used to validate that the value of the `myInput` field is at least 5 characters long. The directive is added to the `input` element as an attribute.

If the value of the `myInput` field is less than 5 characters, the form will not be valid and the user will not be able to submit it.

Here is a list of some of the other useful AngularJS validation directives:

* `ng-maxlength` - Validates that the value of an input field is no longer than a specified number of characters.
* `ng-pattern` - Validates that the value of an input field matches a specified regular expression.
* `ng-required` - Validates that the value of an input field is not empty.

For more information about AngularJS validation directives, please see the [AngularJS Developer Guide](https://docs.angularjs.org/guide/forms).

onelinerhub: [How do I use an AngularJS validation directive?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-validation-directive)