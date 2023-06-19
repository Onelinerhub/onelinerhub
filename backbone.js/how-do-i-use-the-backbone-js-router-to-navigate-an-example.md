# How do I use the Backbone.js Router to navigate an example?
// plain

The Backbone.js Router is used to navigate between different views in an application. It can be used to map routes to functions that will be called when the application navigates to the route.

Below is an example of using the Backbone.js Router to navigate to a view.

```javascript
// Create a new Router
var router = new Backbone.Router();

// Map the route '/example' to the function exampleView
router.route('/example', 'exampleView');

// Create the exampleView function
function exampleView() {
  console.log('Navigated to exampleView');
}

// Navigate to the '/example' route
router.navigate('/example', {trigger: true});

// Output: Navigated to exampleView
```

The code above creates a new Router and maps the route `/example` to a function `exampleView`. Then the `navigate` function is called on the Router with the `/example` route and the `trigger` option set to `true`. This will call the `exampleView` function and output `Navigated to exampleView` to the console.

Parts of the code:
- `var router = new Backbone.Router();`: Creates a new Backbone.js Router.
- `router.route('/example', 'exampleView');`: Maps the route `/example` to the function `exampleView`.
- `function exampleView() {...}`: The function that will be called when the application navigates to the `/example` route.
- `router.navigate('/example', {trigger: true});`: Navigates to the `/example` route and calls the `exampleView` function.

## Helpful links
- [Backbone.js Router Documentation](http://backbonejs.org/#Router)
- [Backbone.js API Documentation](http://backbonejs.org/#Router-navigate)

onelinerhub: [How do I use the Backbone.js Router to navigate an example?](https://onelinerhub.com/backbone.js/how-do-i-use-the-backbone-js-router-to-navigate-an-example)