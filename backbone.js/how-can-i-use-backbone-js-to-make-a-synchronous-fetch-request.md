# How can I use Backbone.js to make a synchronous fetch request?
// plain

Backbone.js provides a `sync` method which can be used to make synchronous fetch requests. It can be used to create, read, update, and delete models in an application. To make a synchronous fetch request, you can use the following code:

```
var MyModel = Backbone.Model.extend({
    urlRoot: '/mymodel'
});

var myModel = new MyModel();
myModel.fetch({
    async: false
});
```

This code will make a synchronous fetch request to the `/mymodel` endpoint. The response data will be stored in the `myModel` object.

The `fetch` method takes an `options` object as an argument. The `async` option can be set to `false` to make the request synchronous.

## Code explanation


- `MyModel` - This is the model class. It has a `urlRoot` property which sets the endpoint for the fetch request.
- `myModel` - This is an instance of the `MyModel` class.
- `fetch` - This is the method used to make the fetch request.
- `options` - This is an object containing options for the `fetch` request.
- `async` - This is a boolean option which determines whether the request is synchronous or asynchronous.

## Helpful links

- [Backbone.sync](http://backbonejs.org/#Sync)
- [Backbone.Model.fetch](http://backbonejs.org/#Model-fetch)

onelinerhub: [How can I use Backbone.js to make a synchronous fetch request?](https://onelinerhub.com/backbone.js/how-can-i-use-backbone-js-to-make-a-synchronous-fetch-request)