# How can I use AngularJS and Webpack 5 together?
// plain

AngularJS and Webpack 5 can be used together to create powerful web applications. Webpack 5 is a module bundler that takes modules with dependencies and generates static assets representing those modules. AngularJS is a JavaScript framework for building client-side web applications.

To use AngularJS and Webpack 5 together, the following steps should be taken:

1. Install Webpack 5:

```
npm install webpack
```

2. Create a `webpack.config.js` file, which will contain the configuration for Webpack 5.

```js
module.exports = {
    entry: './src/main.js',
    output: {
        filename: 'bundle.js',
        path: __dirname + '/dist'
    }
};
```

3. Install AngularJS:

```
npm install angular
```

4. Create an `index.html` file, which will be the entry point for the AngularJS application.

```html
<html>
    <head>
        <title>AngularJS Webpack 5 App</title>
    </head>
    <body>
        <div ng-app="app">
            <div ng-controller="MainController">
                ...
            </div>
        </div>
        <script src="dist/bundle.js"></script>
    </body>
</html>
```

5. Create an `main.js` file, which will contain the AngularJS application code.

```js
var app = angular.module('app', []);

app.controller('MainController', function($scope) {
    // AngularJS code here
});
```

6. Run Webpack 5 to bundle the application code:

```
webpack
```

7. Open the `index.html` file in a browser to see the AngularJS application.

## Helpful links
- [Webpack 5 Documentation](https://webpack.js.org/concepts/)
- [AngularJS Documentation](https://docs.angularjs.org/guide)

onelinerhub: [How can I use AngularJS and Webpack 5 together?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-and-webpack---together)