# How can I migrate from AngularJS to Angular?
// plain

Migrating from AngularJS to Angular can be done in several steps:

1. Install the latest version of Angular CLI:
```
npm install -g @angular/cli
```

2. Create a new Angular project:
```
ng new my-project
```

3. Move your existing AngularJS code into the new project:
- Move all the HTML templates to the `src/app` folder.
- Move all the JavaScript code to the `src/app` folder.
- Move all the CSS and images to the `src/assets` folder.

4. Identify and update any AngularJS-specific code:
- Replace `ng-app` with `ng-app="myApp"` in the HTML template.
- Replace `ng-controller` with `[ngController]` in the HTML template.
- Replace `$scope` with `this` in the JavaScript code.
- Replace `$http` with `HttpClient` in the JavaScript code.

5. Run the project to ensure everything is working:
```
ng serve
```

6. Update the project as needed to take advantage of new Angular features.

7. Deploy your updated project.

For more information on migrating from AngularJS to Angular, see the [official documentation](https://angular.io/guide/upgrade).

onelinerhub: [How can I migrate from AngularJS to Angular?](https://onelinerhub.com/angularjs/how-can-i-migrate-from-angularjs-to-angular)