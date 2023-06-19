# How can I use Angular and Zorro together to create a software application?
// plain

Angular and Zorro can be used together to create a software application by taking advantage of the features of both frameworks.

First, create a new Angular project using the Angular CLI:

```
ng new my-project
```

Next, install the Zorro library into the project:

```
npm install ng-zorro-antd --save
```

Then, import the Zorro modules into the root NgModule of the project:

```
import { NgZorroAntdModule } from 'ng-zorro-antd';

@NgModule({
  imports: [
    NgZorroAntdModule
  ]
})
export class AppModule { }
```

After that, you can use Zorro components in the application, such as the button component:

```
<button nz-button>Click Me</button>
```

You can also use Zorro's form components to create forms and bind them to the application's data model.

Finally, use the Angular CLI to build and deploy the application to a web server.

For more information on using Angular and Zorro together, see the following resources:

- [Zorro Documentation](https://ng.ant.design/docs/introduce/en)
- [Angular CLI Documentation](https://cli.angular.io/docs)
- [Angular Zorro Tutorial](https://www.guru99.com/angular-zorro-tutorial.html)

onelinerhub: [How can I use Angular and Zorro together to create a software application?](https://onelinerhub.com/angularjs/how-can-i-use-angular-and-zorro-together-to-create-a-software-application)