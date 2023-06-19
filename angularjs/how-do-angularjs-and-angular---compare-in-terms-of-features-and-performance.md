# How do AngularJS and Angular 2 compare in terms of features and performance?
// plain

AngularJS and Angular 2 are similar in many ways, but there are also some key differences.

In terms of features, AngularJS is a JavaScript-based open-source front-end web application framework, while Angular 2 is a TypeScript-based open-source web application framework. AngularJS requires the use of controllers and $scope to manage the data for views, whereas Angular 2 uses components and directives. AngularJS uses the traditional Model-View-Controller (MVC) architecture, while Angular 2 uses the Model-View-ViewModel (MVVM) architecture.

In terms of performance, AngularJS has a higher initial loading time compared to Angular 2 due to its complex DOM manipulation. Angular 2 is faster due to its improved change detection and improved rendering.

For example, the following code block shows the difference between the two frameworks in terms of performance:

```
// AngularJS
$scope.data = {
  name: 'John',
  age: 30
};

// Angular 2
@Component({
  selector: 'app-root',
  template: `
    <div>
      {{data.name}} is {{data.age}} years old
    </div>
  `
})
export class AppComponent {
  data = {
    name: 'John',
    age: 30
  };
}
```

This code block does not produce any output.

In summary, AngularJS and Angular 2 are similar in terms of features but differ in terms of performance. AngularJS has a higher initial loading time but Angular 2 is faster due to its improved change detection and improved rendering.

## Helpful links

- [AngularJS Documentation](https://angularjs.org/docs)
- [Angular 2 Documentation](https://angular.io/docs)

onelinerhub: [How do AngularJS and Angular 2 compare in terms of features and performance?](https://onelinerhub.com/angularjs/how-do-angularjs-and-angular---compare-in-terms-of-features-and-performance)