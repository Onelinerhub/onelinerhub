# How do I use an AngularJS template?
// plain

An AngularJS template is an HTML page that contains AngularJS-specific elements and attributes. To use an AngularJS template, you'll need to include the AngularJS library in the `<head>` of the HTML page.

```html
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
</head>
```

Once the AngularJS library is included, you can start adding AngularJS-specific elements and attributes to the HTML page. For example, you can add the `ng-app` attribute to the `<html>` tag, which will tell AngularJS to load the application when the page is loaded.

```html
<html ng-app="myApp">
  ...
</html>
```

You can also add the `ng-controller` attribute to an HTML element, which will tell AngularJS to load the controller associated with the HTML element.

```html
<div ng-controller="MyController">
  ...
</div>
```

Finally, you can add the `{{ }}` syntax to your HTML page, which will tell AngularJS to evaluate the expression inside the `{{ }}` syntax and display the result.

```html
<div>
  The result is {{ 1 + 1 }}
</div>
```

## Output example

```
The result is 2
```

You can find more information about using AngularJS templates in the [AngularJS Documentation](https://docs.angularjs.org/guide/templates).

onelinerhub: [How do I use an AngularJS template?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-template)