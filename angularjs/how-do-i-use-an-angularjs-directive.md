# How do I use an AngularJS directive?
// plain

An AngularJS directive is a JavaScript object that augments an HTML element with custom behavior. To use a directive, you first need to include the directive in your HTML page. This can be done by either adding an attribute to the HTML element or by adding an element.

For example, the following code adds the `ng-app` directive to the `<html>` element:
```html
<html ng-app>
```

The `ng-app` directive tells AngularJS to treat the element and its children as an AngularJS application.

Once the directive has been included in the HTML page, you can use it to add behavior to the element. For example, the following code uses the `ng-model` directive to bind the value of the `<input>` element to the `name` property of the `$scope` object:
```html
<input type="text" ng-model="name" />
```

When the user types into the `<input>` element, the value of the `name` property of the `$scope` object is updated.

Directives can also be used to create custom elements and attributes. For example, the following code creates a new element called `<my-directive>`:
```html
<my-directive></my-directive>
```

The directive can then be used to add custom behavior to the element. For example, the following code uses the `ng-click` directive to call a function when the element is clicked:
```html
<my-directive ng-click="myFunction()"></my-directive>
```

When the element is clicked, the `myFunction()` function is called.

Directives are a powerful feature of AngularJS and can be used to create custom elements and attributes, as well as bind data to HTML elements.

## Helpful links
- [AngularJS Directives](https://docs.angularjs.org/guide/directive)
- [AngularJS ng-app Directive](https://docs.angularjs.org/api/ng/directive/ngApp)
- [AngularJS ng-model Directive](https://docs.angularjs.org/api/ng/directive/ngModel)
- [AngularJS ng-click Directive](https://docs.angularjs.org/api/ng/directive/ngClick)

onelinerhub: [How do I use an AngularJS directive?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-directive)