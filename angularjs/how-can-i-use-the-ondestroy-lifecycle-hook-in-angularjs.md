# How can I use the onDestroy lifecycle hook in AngularJS?
// plain

The onDestroy lifecycle hook in AngularJS is a method that is called when a component is about to be destroyed. It is a good practice to use this hook to perform any necessary clean up tasks, such as unsubscribing from observables, cancelling any pending HTTP requests, and resetting any model data.

## Example code

```
import { Component, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent implements OnDestroy {
  ngOnDestroy() {
    // Perform any necessary clean up tasks here
  }
}
```

The code above shows an example of how to use the onDestroy lifecycle hook in an AngularJS component. The example imports the OnDestroy interface from the @angular/core library and implements it in the component. The ngOnDestroy() method is then called when the component is about to be destroyed, allowing the developer to perform any necessary clean up tasks.

## Code explanation


- `import { Component, OnDestroy } from '@angular/core';`: This line imports the Component and OnDestroy interfaces from the @angular/core library.
- `@Component({ ... })`: This is the decorator that is used to define the component.
- `export class ExampleComponent implements OnDestroy { ... }`: This line exports the ExampleComponent class and implements the OnDestroy interface.
- `ngOnDestroy() { ... }`: This is the method that is called when the component is about to be destroyed. This is where the developer can perform any necessary clean up tasks.

## Helpful links

- [Angular Documentation - Lifecycle Hooks](https://angular.io/guide/lifecycle-hooks)
- [Angular Tutorial - OnDestroy Lifecycle Hook](https://www.javatpoint.com/angular-on-destroy)

onelinerhub: [How can I use the onDestroy lifecycle hook in AngularJS?](https://onelinerhub.com/angularjs/how-can-i-use-the-ondestroy-lifecycle-hook-in-angularjs)