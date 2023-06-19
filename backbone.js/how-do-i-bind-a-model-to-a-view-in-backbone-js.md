# How do I bind a model to a view in Backbone.js?
// plain

Backbone.js provides an easy way to bind models to views. The `Backbone.View.extend()` function is used to create a view and the `Backbone.Model.extend()` is used to create a model.

The `render()` method is used to bind the model to the view. This method is called when the view is instantiated.

The following example shows how to bind a model to a view:

```javascript
// Create model
var Person = Backbone.Model.extend({
  defaults: {
    name: '',
    age: 0
  }
});

// Create view
var PersonView = Backbone.View.extend({
  el: '#person-container',
  initialize: function() {
    this.render();
  },
  render: function() {
    this.$el.html(this.model.get('name') + ' is ' + this.model.get('age') + ' years old.');
  }
});

// Create model instance
var person = new Person({ name: 'John', age: 25 });

// Create view instance
var personView = new PersonView({ model: person });
```

The output of the above code will be: `John is 25 years old.`

## Code explanation


1. `Backbone.Model.extend()`: Used to create a model.
2. `Backbone.View.extend()`: Used to create a view.
3. `render()`: Used to bind the model to the view.
4. `Person`: Model instance.
5. `PersonView`: View instance.
6. `this.model.get()`: Used to get the model properties.
7. `this.$el.html()`: Used to set the view HTML.

## Helpful links

- [Backbone.js Documentation](http://backbonejs.org/)
- [Backbone.Model.extend()](http://backbonejs.org/#Model-extend)
- [Backbone.View.extend()](http://backbonejs.org/#View-extend)

onelinerhub: [How do I bind a model to a view in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-bind-a-model-to-a-view-in-backbone-js)