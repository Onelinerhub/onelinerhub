# How do I upgrade to the latest version of AngularJS?
// plain

Upgrading to the latest version of AngularJS is a relatively straightforward process.

1. First, check the [AngularJS website](https://angularjs.org/) to find out the latest version number.

2. Next, install the latest version of AngularJS using the command line. For example, to install version 1.7.9:

```
npm install angular@1.7.9
```

3. After the installation is complete, open the `index.html` file and update the version number in the `<script>` tag:

```
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.9/angular.min.js"></script>
```

4. Finally, open the `app.js` file and update the version number in the `angular.module` method:

```
angular.module('myApp', ['ngRoute', 'ngAnimate', '1.7.9']);
```

That's it! You have now successfully upgraded to the latest version of AngularJS.

Note: If you're using a more recent version of AngularJS (e.g. 2.0+), the installation and updating process may be slightly different. Refer to the [AngularJS documentation](https://docs.angularjs.org/guide/upgrading) for more information.

onelinerhub: [How do I upgrade to the latest version of AngularJS?](https://onelinerhub.com/angularjs/how-do-i-upgrade-to-the-latest-version-of-angularjs)