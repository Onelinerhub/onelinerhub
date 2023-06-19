# How do I save a Backbone.js model?
// plain

Saving a Backbone.js model is done using the `save()` method. This method will persist the model to the server and will fire an `"sync"` event when the model is successfully saved.

Here's an example of using `save()` to persist a model:

```javascript
var myModel = new Backbone.Model({
  name: 'John Doe'
});

myModel.save();
```

In the example above, the `save()` method will send an `HTTP PUT` request to the server with the model data. If successful, the server will return an `HTTP 200` response and the `"sync"` event will be fired.

The `save()` method also takes an optional `options` parameter. This can be used to customize the request, such as setting the `HTTP method` or providing additional data to be sent to the server. Here's an example:

```javascript
var myModel = new Backbone.Model({
  name: 'John Doe'
});

myModel.save({}, {
  type: 'POST',
  data: {
    age: 30
  }
});
```

In this example, an `HTTP POST` request will be sent to the server with the model data and the additional `age` parameter.

#### Parts of code explained

* `save()` - This method will persist the model to the server and will fire an `"sync"` event when the model is successfully saved.
* `options` - This parameter can be used to customize the request, such as setting the `HTTP method` or providing additional data to be sent to the server.

#### Relevant Links

* [Backbone.js Documentation - Save](http://backbonejs.org/#Model-save)

onelinerhub: [How do I save a Backbone.js model?](https://onelinerhub.com/backbone.js/how-do-i-save-a-backbone-js-model)