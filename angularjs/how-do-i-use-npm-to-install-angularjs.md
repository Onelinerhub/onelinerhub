# How do I use npm to install AngularJS?
// plain

NPM (Node Package Manager) is a command line utility used for installing and managing packages for Node.js. It can also be used to install AngularJS, a popular JavaScript framework for developing single-page applications.

To install AngularJS using NPM, open a terminal window and run the following command:

```
npm install angular
```

This will install the latest version of AngularJS. To install a specific version, you can specify the version number after the package name. For example, to install version 1.3.0:

```
npm install angular@1.3.0
```

The above command will install the AngularJS package in the `node_modules` folder of your project. You can then include the package in your HTML file using a `<script>` tag.

```html
<script src="node_modules/angular/angular.min.js"></script>
```

You can also use NPM to install other packages related to AngularJS, such as the Angular CLI (Command Line Interface) or the Angular UI Bootstrap library.

## Helpful links

- [NPM Documentation](https://docs.npmjs.com/)
- [AngularJS Documentation](https://angularjs.org/)
- [Angular CLI Documentation](https://cli.angular.io/)
- [Angular UI Bootstrap Documentation](https://angular-ui.github.io/bootstrap/)

onelinerhub: [How do I use npm to install AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-npm-to-install-angularjs)