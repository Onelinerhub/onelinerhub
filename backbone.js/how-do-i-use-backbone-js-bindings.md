# How do I use Backbone.js bindings?
// plain

Backbone.js bindings allow you to connect your data to the DOM. This means that when your data changes, the DOM automatically updates to reflect the new data.

To use Backbone.js bindings, you need to create a model and view. The model is responsible for storing the data, and the view is responsible for displaying it.

## Example code

```
// Create a model
var Person = Backbone.Model.extend({
  defaults: {
    name: 'John Doe',
    age: 30
  }
});

// Create a view
var PersonView = Backbone.View.extend({
  el: '#person',

  initialize: function(){
    this.render();
  },

  render: function(){
    this.$el.html(this.model.get('name') + ' (' + this.model.get('age') + ')');
  }
});

// Create an instance of the model
var person = new Person();

// Create an instance of the view
var personView = new PersonView({ model: person });
```

The code above creates a model and view for a person. The model stores the person's name and age, and the view displays it on the page.

When the data in the model is changed, the view will automatically update to reflect the new data. For example, if the person's name is changed to 'Jane Doe':

```
person.set('name', 'Jane Doe');
```

The view will update to show 'Jane Doe (30)'.

For more information on Backbone.js bindings, see the [Backbone.js documentation](http://backbonejs.org/#View-binding).

onelinerhub: [How do I use Backbone.js bindings?](https://onelinerhub.com/backbone.js/how-do-i-use-backbone-js-bindings)