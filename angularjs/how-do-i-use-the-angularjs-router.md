# How do I use the AngularJS router?
// plain

The AngularJS router is a service that helps you to set up navigation between different views of your application. It allows you to define routes, which are mappings between URLs and the components that will be displayed when those URLs are accessed.

To use the AngularJS router, you first need to add the `ngRoute` module to your application.

```
angular.module('myApp', ['ngRoute'])
```

Then, you need to configure the routes for your application. This is done using the `$routeProvider` service.

```
angular.module('myApp', ['ngRoute'])
  .config(function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home.html',
        controller: 'HomeController'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutController'
      });
  });
```

The above code defines two routes, `/` and `/about`, which will display the `home.html` and `about.html` views respectively. The `HomeController` and `AboutController` controllers will be used to handle the logic for each view.

Finally, you need to add a `<base>` tag to your `index.html` file, which will be used by the router to handle navigation.

```
<base href="/">
```

Once you have done this, you can use the `$location` service to navigate to different routes in your application. For example:

```
$location.path('/about');
```

This will navigate to the `/about` route, which will display the `about.html` view.

## Helpful links
- [AngularJS Router Documentation](https://docs.angularjs.org/api/ngRoute)
- [AngularJS Tutorial](https://www.tutorialspoint.com/angularjs/)

onelinerhub: [How do I use the AngularJS router?](https://onelinerhub.com/angularjs/how-do-i-use-the-angularjs-router)