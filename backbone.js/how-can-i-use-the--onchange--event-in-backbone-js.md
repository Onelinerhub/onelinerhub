# How can I use the "onchange" event in Backbone.js?
// plain

The `onchange` event can be used in Backbone.js to detect when a model's attribute has been changed. It is triggered when a `set` or `change` event is fired on the model.

For example, if a model had an attribute `name` and it was changed, the `onchange` event would be triggered:

```js
var Model = Backbone.Model.extend({
  initialize: function() {
    this.on('change', function() {
      console.log('Name changed!');
    });
  }
});

var model = new Model({ name: 'John' });
model.set('name', 'Bob');

// Output: 'Name changed!'
```

The `onchange` event can also take a callback function as an argument:

```js
var Model = Backbone.Model.extend({
  initialize: function() {
    this.on('change', function(model) {
      console.log('Name changed to ' + model.get('name'));
    });
  }
});

var model = new Model({ name: 'John' });
model.set('name', 'Bob');

// Output: 'Name changed to Bob'
```

The callback function will be passed the model as an argument, which can be used to get the changed attribute's new value.

The `onchange` event is part of the [Backbone.Events API](http://backbonejs.org/#Events), which provides methods for binding and triggering custom events on a Backbone object.

## Helpful links

- [Backbone.Events API](http://backbonejs.org/#Events)
- [Backbone.Model.set()](http://backbonejs.org/#Model-set)
- [Backbone.Model.change()](http://backbonejs.org/#Model-change)

onelinerhub: [How can I use the "onchange" event in Backbone.js?](https://onelinerhub.com/backbone.js/how-can-i-use-the--onchange--event-in-backbone-js)