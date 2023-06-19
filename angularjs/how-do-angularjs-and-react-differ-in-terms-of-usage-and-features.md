# How do AngularJS and React differ in terms of usage and features?
// plain

AngularJS and React are two popular front-end JavaScript frameworks. Although they share some similarities, they have some key differences in terms of usage and features.

**Usage**
AngularJS is a full-featured framework, which means that it provides a complete set of tools for developing a web application. React, on the other hand, is a library, which means it only provides the view layer of a web application.

**Features**

1. **Data Binding**: AngularJS uses two-way data binding, which means that when a model is changed, the view is updated automatically and vice versa. React, however, uses one-way data binding, which means that the view is updated only when the state of the component is changed.

2. **DOM Manipulation**: AngularJS uses a real DOM (Document Object Model) which means it can update the DOM directly when the model changes. React, however, uses a virtual DOM, which means it creates a copy of the DOM and makes the changes to the copy first.

3. **Routing**: AngularJS provides a built-in router module which can be used to handle navigation between different views in the application. React, on the other hand, does not provide a built-in router and it needs to be integrated with a third-party library.

```
Example code

// AngularJS
var app = angular.module('myApp', ['ngRoute']);
app.config(function($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'views/home.html',
      controller: 'HomeController'
    })
    .when('/about', {
      templateUrl: 'views/about.html',
      controller: 'AboutController'
    })
    .otherwise({
      redirectTo: '/'
    });
});

// React
import { BrowserRouter as Router, Route } from 'react-router-dom';

ReactDOM.render(
  <Router>
    <div>
      <Route exact path="/" component={Home} />
      <Route path="/about" component={About} />
    </div>
  </Router>,
  document.getElementById('root')
);
```

## Helpful links

- [AngularJS Docs](https://angularjs.org/)
- [React Docs](https://reactjs.org/)

onelinerhub: [How do AngularJS and React differ in terms of usage and features?](https://onelinerhub.com/angularjs/how-do-angularjs-and-react-differ-in-terms-of-usage-and-features)