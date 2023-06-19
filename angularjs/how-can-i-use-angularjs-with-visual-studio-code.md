# How can I use AngularJS with Visual Studio Code?
// plain

AngularJS can be used with Visual Studio Code (VSCode) to create dynamic web applications. To get started, you will need to install the [Angular Language Service extension](https://marketplace.visualstudio.com/items?itemName=Angular.ng-template) and the [TypeScript compiler](https://www.npmjs.com/package/typescript). Once installed, you can create an AngularJS project by using the `ng new` command in the VSCode terminal.

You can then write code in the VSCode editor and use the Angular Language Service to get autocomplete and type checking. For example, you can write the following code in the editor:

```
<div ng-app="myApp">
    <div ng-controller="myController">
        {{message}}
    </div>
</div>

<script>
    var app = angular.module('myApp', []);
    app.controller('myController', function($scope) {
        $scope.message = 'Hello World!';
    });
</script>
```

This code will output the following in the browser:

```
Hello World!
```

The Angular Language Service will also provide helpful warnings and errors to help you debug your code.

In addition to the Angular Language Service, VSCode also provides useful features such as code refactoring, debugging, and IntelliSense. With these features, you can quickly and easily develop AngularJS applications in VSCode.

onelinerhub: [How can I use AngularJS with Visual Studio Code?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-with-visual-studio-code)