# How can I use Backbone.js to update a view when a model changes?
// plain

Backbone.js provides an event-based system for updating views when a model changes. To use this system, you must first create a model and view.

To create a model, you can use the `Backbone.Model` constructor. For example:

```js
var MyModel = Backbone.Model.extend({
  defaults: {
    text: 'Hello World'
  }
});
```

To create a view, you can use the `Backbone.View` constructor. For example:

```js
var MyView = Backbone.View.extend({
  initialize: function() {
    this.listenTo(this.model, 'change', this.render);
  },
  render: function() {
    this.$el.html(this.model.get('text'));
  }
});
```

This view will listen to changes on the model and call the `render` function whenever the model changes. To create an instance of the view, you can do something like this:

```js
var myModel = new MyModel();
var myView = new MyView({ model: myModel });
```

Now, whenever the model changes, the view will update. For example, if you run the following code:

```js
myModel.set('text', 'Goodbye World');
```

The view will be updated with the new value of `text`.

## Parts and Explanation

1. `Backbone.Model` constructor - used to create a model.
2. `Backbone.View` constructor - used to create a view.
3. `listenTo` - used to listen for changes on the model.
4. `render` - the function to call when the model changes.
5. `this.model.get('text')` - used to get the value of `text` from the model.
6. `myModel.set('text', 'Goodbye World')` - used to set the value of `text` on the model.

## Relevant Links

- [Backbone.js](http://backbonejs.org/)
- [Backbone.Model](http://backbonejs.org/#Model)
- [Backbone.View](http://backbonejs.org/#View)

onelinerhub: [How can I use Backbone.js to update a view when a model changes?](https://onelinerhub.com/backbone.js/how-can-i-use-backbone-js-to-update-a-view-when-a-model-changes)