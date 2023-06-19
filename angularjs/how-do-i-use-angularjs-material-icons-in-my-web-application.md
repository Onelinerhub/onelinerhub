# How do I use AngularJS Material Icons in my web application?
// plain

To use AngularJS Material Icons in your web application, you'll need to include the AngularJS Material library in your HTML page.

```html
<head>
  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/angular_material/1.1.0/angular-material.min.css">
</head>
```

Then add the AngularJS Material Icons module as a dependency to your AngularJS application.

```javascript
angular.module('myApp', ['ngMaterial', 'ngMessages', 'material.svgAssetsCache']);
```

Next, you can use the `md-icon` directive to display icons in your application.

```html
<md-icon md-svg-icon="my-icon"></md-icon>
```

The `md-svg-icon` attribute tells AngularJS Material which icon to display. You can also set the icon size with the `md-font-set` attribute.

```html
<md-icon md-svg-icon="my-icon" md-font-set="my-iconset"></md-icon>
```

You can also use the `md-icon-button` directive to display an icon button.

```html
<md-icon-button md-svg-icon="my-icon" aria-label="My Icon Button"></md-icon-button>
```

For more information, see the [AngularJS Material Icons Documentation](https://material.angularjs.org/latest/demo/icon).

onelinerhub: [How do I use AngularJS Material Icons in my web application?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-material-icons-in-my-web-application)