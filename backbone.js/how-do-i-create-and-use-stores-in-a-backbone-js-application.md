# How do I create and use stores in a Backbone.js application?
// plain

Creating and using stores in a Backbone.js application is done by creating a Model or Collection and then setting the `localStorage` property on it.

For example, to create a Model with localStorage and save it:

```
var Todo = Backbone.Model.extend({
  localStorage: new Backbone.LocalStorage("todo-store")
});

var todo = new Todo({name: "My Todo"});
todo.save();
```

To use the stored values, you can call `fetch()` on the Model or Collection:

```
todo.fetch();
```

The parts of this code are:

1. `var Todo = Backbone.Model.extend({` - creating a Backbone Model
2. `localStorage: new Backbone.LocalStorage("todo-store")` - setting the localStorage property on the Model
3. `var todo = new Todo({name: "My Todo"});` - creating a new instance of the Model
4. `todo.save();` - saving the Model to localStorage
5. `todo.fetch();` - fetching the Model from localStorage

## Helpful links

- [Backbone.js Documentation](http://backbonejs.org/)
- [Backbone.LocalStorage Documentation](https://github.com/jeromegn/Backbone.localStorage)

onelinerhub: [How do I create and use stores in a Backbone.js application?](https://onelinerhub.com/backbone.js/how-do-i-create-and-use-stores-in-a-backbone-js-application)