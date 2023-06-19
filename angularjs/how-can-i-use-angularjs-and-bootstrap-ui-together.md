# How can I use AngularJS and Bootstrap UI together?
// plain

AngularJS and Bootstrap UI can be used together to create dynamic, responsive web applications. To get started, include the Bootstrap CSS and JavaScript files in the HTML page, then add the AngularJS script.

```
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.7/angular.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</head>
```

After including the necessary files, you can use components from both AngularJS and Bootstrap UI in the same application. For example, you can create a simple form using Bootstrap UI and then add AngularJS directives and controllers to provide data binding and validation.

```
<div class="container">
    <form name="myForm" novalidate>
        <div class="form-group">
            <label>Name</label>
            <input type="text" name="name" class="form-control" ng-model="name" required />
            <span ng-show="myForm.name.$error.required">Name is required</span>
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-primary" ng-disabled="myForm.$invalid">Submit</button>
        </div>
    </form>
</div>
```

In this example, the `<form>` element and `<input>` elements are using Bootstrap UI classes to style them, while the `ng-model`, `ng-show`, and `ng-disabled` directives are from AngularJS.

- `<form>` element: defines the form
- `<input>` element: provides the input field
- `ng-model` directive: binds the input to a variable in the controller
- `ng-show` directive: displays the error message if the input is invalid
- `ng-disabled` directive: disables the submit button if the form is invalid

For more information on using AngularJS and Bootstrap UI together, see the following links:

- [Using Bootstrap with Angular](https://scotch.io/tutorials/using-bootstrap-with-angular)
- [AngularJS and Bootstrap](https://www.codeproject.com/Articles/1113008/AngularJS-and-Bootstrap)

onelinerhub: [How can I use AngularJS and Bootstrap UI together?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-and-bootstrap-ui-together)