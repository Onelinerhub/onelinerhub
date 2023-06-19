# How do I use AngularJS and Bower together?
// plain

Using AngularJS and Bower together can be a great way to manage the dependencies of your web application. Bower is a package manager for the web, and it can be used to install and manage the different libraries and frameworks used in an AngularJS application.

To use Bower with AngularJS, first install Bower using npm.

```
npm install -g bower
```

Once Bower is installed, you can use it to install the AngularJS library.

```
bower install angular
```

This will create a folder called `bower_components` in your project directory, which contains the AngularJS library. You can then include the AngularJS library in your HTML file by adding the following line:

```
<script src="bower_components/angular/angular.js"></script>
```

You can also use Bower to install other libraries and frameworks used in an AngularJS application, such as jQuery and Bootstrap.

## Code explanation


1. `npm install -g bower`: Installs Bower package manager.
2. `bower install angular`: Installs the AngularJS library.
3. `<script src="bower_components/angular/angular.js"></script>`: Includes the AngularJS library in your HTML file.

## Helpful links

- https://bower.io/
- https://angularjs.org/

onelinerhub: [How do I use AngularJS and Bower together?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-and-bower-together)