# How can I use Backbone.js to solve a specific problem?
// plain

Backbone.js is a JavaScript library that provides structure to web applications by providing models with key-value binding and custom events, collections with a rich API of enumerable functions, views with declarative event handling, and connects it all to your existing API over a RESTful JSON interface. It is a great tool to use when developing single page applications (SPAs).

For example, if you wanted to create a to-do list application, you could create a model for each to-do item, a collection to store all the to-do items, and a view to render the list of to-dos.

```javascript
// Model
var Todo = Backbone.Model.extend({
  defaults: {
    title: '',
    completed: false
  }
});

// Collection
var TodoList = Backbone.Collection.extend({
  model: Todo
});

// View
var TodoView = Backbone.View.extend({
  tagName: 'li',
  template: _.template("<%= title %>"),
  render: function(){
    this.$el.html( this.template( this.model.toJSON() ) );
    return this;
  }
});
```

Then, you could create an instance of the collection and view.

```javascript
// Create a collection
var todos = new TodoList();

// Create a view
var todoView = new TodoView({ model: todos });
```

Finally, you can use the `add` method to add to-dos to the collection and render the view.

```javascript
// Add a to-do
todos.add({ title: 'Do laundry' });

// Render the view
todoView.render();
```

The output of the above code would be an `li` element with the text "Do laundry".

## Helpful links
* [Backbone.js Documentation](http://backbonejs.org/)
* [Getting Started with Backbone.js](https://scotch.io/tutorials/getting-started-with-backbone-js)
* [Building a Todo App with Backbone.js](https://scotch.io/tutorials/building-a-todo-app-with-backbone-js-and-localstorage)

onelinerhub: [How can I use Backbone.js to solve a specific problem?](https://onelinerhub.com/backbone.js/how-can-i-use-backbone-js-to-solve-a-specific-problem)