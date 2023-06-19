# How do I create a controller in Backbone.js?
// plain

Creating a controller in Backbone.js is done by extending the Backbone.Router object.

An example of a controller with a single route is as follows:

```
var AppRouter = Backbone.Router.extend({
    routes: {
        "": "home"
    },
    home: function(){
        console.log("home route");
    }
});

var app_router = new AppRouter();
Backbone.history.start();
```

This code will output `home route` when the application is run.

## Code explanation


- `var AppRouter = Backbone.Router.extend({`: This line creates a new router object and extends the Backbone.Router object.

- `routes: { "": "home" },`: This line defines a single route, which is the home route.

- `home: function(){ console.log("home route"); }`: This line defines the callback function for the home route, which logs `home route` to the console.

- `var app_router = new AppRouter();`: This line creates a new instance of the AppRouter object.

- `Backbone.history.start();`: This line starts the routers history.

For more information on creating controllers in Backbone.js, see the [Backbone.js documentation](http://backbonejs.org/#Router).

onelinerhub: [How do I create a controller in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-create-a-controller-in-backbone-js)