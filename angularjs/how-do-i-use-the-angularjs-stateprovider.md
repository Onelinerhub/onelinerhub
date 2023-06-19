# How do I use the AngularJS StateProvider?
// plain

The AngularJS StateProvider is a service that allows you to define the states of your application. It is used to manage the different views of your application.

To use the StateProvider, you need to include the `ui-router` module in your application.

```
angular.module('myApp', ['ui-router'])
```

Then you can set up your states using the `stateProvider` service.

```
.config(function($stateProvider) {
  $stateProvider
    .state('home', {
      url: '/home',
      templateUrl: 'home.html'
    })
    .state('about', {
      url: '/about',
      templateUrl: 'about.html'
    });
})
```

In the example above, two states are defined, `home` and `about`. The `url` is the path to the state, and the `templateUrl` is the template to be loaded when the state is active.

You can also define parameters and resolve functions for each state.

```
.state('post', {
  url: '/post/:postId',
  templateUrl: 'post.html',
  params: {
    postId: null
  },
  resolve: {
    post: function($stateParams) {
      // Get the post with the specified postId
      return PostService.getPost($stateParams.postId);
    }
  }
})
```

In the example above, the `postId` parameter is defined, and a `resolve` function is used to get the post with the specified `postId`.

## Helpful links

- [AngularJS StateProvider Documentation](https://ui-router.github.io/ng1/docs/latest/index.html#/api/ui.router.state.$stateProvider)

onelinerhub: [How do I use the AngularJS StateProvider?](https://onelinerhub.com/angularjs/how-do-i-use-the-angularjs-stateprovider)