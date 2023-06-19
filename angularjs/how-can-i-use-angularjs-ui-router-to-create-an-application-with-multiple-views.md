# How can I use AngularJS UI Router to create an application with multiple views?
// plain

AngularJS UI Router is a routing framework for AngularJS applications that allows you to organize the different components of your application into a state machine. Each state corresponds to a "place" in the application, and can be associated with a URL, or even nested within other states.

To create an application with multiple views using AngularJS UI Router, you can use the `$stateProvider` service to define the different states of your application. For example:

```js
$stateProvider
  .state('home', {
    url: '/home',
    templateUrl: 'views/home.html',
    controller: 'HomeController'
  })
  .state('about', {
    url: '/about',
    templateUrl: 'views/about.html',
    controller: 'AboutController'
  })
```

This code will define two states, `home` and `about`, each with its own URL, template and controller.

You can then use the `ui-sref` directive to link between the different states of your application, for example:

```html
<a ui-sref="home">Home</a>
<a ui-sref="about">About</a>
```

This will create two links that will take the user to the `home` and `about` states respectively.

## Helpful links

- [AngularJS UI Router Documentation](https://ui-router.github.io/docs)
- [AngularJS UI Router Tutorial](https://scotch.io/tutorials/angular-routing-using-ui-router)

onelinerhub: [How can I use AngularJS UI Router to create an application with multiple views?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-ui-router-to-create-an-application-with-multiple-views)