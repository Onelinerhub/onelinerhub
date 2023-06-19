# How do I set headers in Backbone.js?
// plain

Backbone.js provides a way to set headers for all requests made from the application. This can be done by setting the `headers` property in the `sync` method of the model or collection.

For example, if you want to set a `Authorization` header on all requests, you can do the following:

```javascript
MyModel = Backbone.Model.extend({
  sync: function(method, model, options) {
    options.headers = {
      'Authorization': 'Bearer <token>'
    };
    return Backbone.sync(method, model, options);
  }
});
```

The `sync` method takes three parameters:

- `method`: The HTTP method to use for the request (e.g. `GET`, `POST`, `PUT`, etc).
- `model`: The model or collection that is being synced.
- `options`: An options object containing the headers to be set.

The `options` object is passed to the `Backbone.sync` method, which is responsible for making the actual request.

You can also set headers on a per-request basis by passing the `headers` option when calling `sync` directly. For example:

```javascript
MyModel.fetch({
  headers: {
    'Authorization': 'Bearer <token>'
  }
});
```

## Helpful links

- [Backbone.sync](http://backbonejs.org/#Sync)
- [Backbone.Model.fetch](http://backbonejs.org/#Model-fetch)

onelinerhub: [How do I set headers in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-set-headers-in-backbone-js)