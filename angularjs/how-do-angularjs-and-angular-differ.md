# How do AngularJS and Angular differ?
// plain

AngularJS and Angular are two different frameworks that have been created by Google. AngularJS is a JavaScript-based open-source front-end web application framework, while Angular is a TypeScript-based open-source web application framework.

**Example code block in AngularJS**
```
<html ng-app>
    <head>
        <title>AngularJS Example</title>
    </head>
    <body>
        <div>
            <h2>Hello {{name}}</h2>
        </div>
    </body>
</html>
```

**Example code block in Angular**
```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Angular Example';
}
```

The main difference between AngularJS and Angular is that AngularJS is a JavaScript-based framework, while Angular is a TypeScript-based framework. AngularJS is based on the Model-View-Controller (MVC) design pattern, while Angular is based on the Component-Service architecture. AngularJS is an older framework and is considered to be easier to learn than Angular, while Angular is considered to be more modern and powerful.

**List of code parts with detailed explanation**
1. `<html ng-app>` - This is the directive that is used to define an AngularJS application.
2. `@Component` - This is a decorator function that is used to define the components in an Angular application.
3. `selector` - This is a property that is used to specify the HTML element that the component will be associated with.
4. `templateUrl` - This is a property that is used to specify the HTML template that will be used to render the component.
5. `styleUrls` - This is a property that is used to specify the stylesheets that will be used to style the component.

**List of relevant links**
- [AngularJS Documentation](https://docs.angularjs.org/guide)
- [Angular Documentation](https://angular.io/docs)

onelinerhub: [How do AngularJS and Angular differ?](https://onelinerhub.com/angularjs/how-do-angularjs-and-angular-differ)