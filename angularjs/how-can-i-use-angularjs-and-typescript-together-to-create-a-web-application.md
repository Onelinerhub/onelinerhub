# How can I use AngularJS and TypeScript together to create a web application?
// plain

AngularJS and TypeScript can be used together to create a web application. TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. It can be used to write AngularJS applications in a type-safe manner.

The following example shows how to create a simple AngularJS application in TypeScript:

```typescript
// app.ts
import { NgModule, Component } from '@angular/core';

@Component({
  selector: 'my-app',
  template: `<h1>Hello {{name}}!</h1>`
})
class AppComponent {
  name: string = 'World';
}

@NgModule({
  declarations: [ AppComponent ],
  bootstrap: [ AppComponent ]
})
class AppModule {}
```

The code above is a simple AngularJS application written in TypeScript. It imports the `NgModule` and `Component` decorators from `@angular/core` and uses them to define a `AppComponent` and an `AppModule`. The `AppComponent` has a `name` property and a template that displays the value of the `name` property.

Finally, the `AppModule` is bootstrapped to run the application.

## Helpful links
- [AngularJS](https://angularjs.org/)
- [TypeScript](https://www.typescriptlang.org/)

onelinerhub: [How can I use AngularJS and TypeScript together to create a web application?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-and-typescript-together-to-create-a-web-application)