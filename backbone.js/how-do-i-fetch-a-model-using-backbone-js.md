# How do I fetch a model using Backbone.js?
// plain

To fetch a model using Backbone.js, you can use the `fetch()` method. This method will make an AJAX request to the server and return the model's data.

For example:
```javascript
var model = new Backbone.Model();
model.fetch({
  success: function(model, response) {
    console.log(response);
  }
});
```
The output of this example would be the data returned from the server.

The `fetch()` method has several options that you can pass in:

* `url`: The URL of the server endpoint to fetch the model from
* `data`: Data to be sent to the server with the request
* `success`: A callback to be called when the request is successful
* `error`: A callback to be called when the request fails

For more information, see the [Backbone.js documentation](http://backbonejs.org/#Model-fetch).

onelinerhub: [How do I fetch a model using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-fetch-a-model-using-backbone-js)