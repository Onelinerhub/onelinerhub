# How can I create an editable AngularJS application?
// plain

To create an editable AngularJS application, you can use the `ng-model` directive. This directive binds the value of HTML controls (input, select, textarea) to application data. For example, the following code block creates an input field that is bound to the `name` variable:

```
<input type="text" ng-model="name">
```

The `name` variable can be used to store and access the value of the input field. The value of `name` will be updated when the user edits the input field.

You can also use the `ng-submit` directive to create a form that can be used to submit user input. The following example code block creates a form with two input fields and a submit button:

```
<form ng-submit="submitForm()">
  <input type="text" ng-model="firstName">
  <input type="text" ng-model="lastName">
  <button type="submit">Submit</button>
</form>
```

The `submitForm()` function can be used to process the form data.

Finally, you can use the `ng-click` directive to create buttons that can be used to perform actions. The following example code block creates a button that logs the value of the `name` variable to the console when clicked:

```
<button ng-click="logName()">Log Name</button>

<script>
  function logName() {
    console.log(name);
  }
</script>
```

When the `logName()` function is called, the value of the `name` variable will be logged to the console.

## Helpful links

- [ng-model](https://docs.angularjs.org/api/ng/directive/ngModel)
- [ng-submit](https://docs.angularjs.org/api/ng/directive/ngSubmit)
- [ng-click](https://docs.angularjs.org/api/ng/directive/ngClick)

onelinerhub: [How can I create an editable AngularJS application?](https://onelinerhub.com/angularjs/how-can-i-create-an-editable-angularjs-application)