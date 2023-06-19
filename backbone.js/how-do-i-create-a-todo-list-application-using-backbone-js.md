# How do I create a todo list application using Backbone.js?
// plain

To create a todo list application using Backbone.js, you'll need a few pieces of code.

1. First, create a model for your todo list item. This will include properties for the item's title, description, and completion status.

```javascript
var Todo = Backbone.Model.extend({
    defaults: {
        title: '',
        description: '',
        completed: false
    }
});
```

2. Next, create a collection to store your todo list items.

```javascript
var TodoList = Backbone.Collection.extend({
    model: Todo
});
```

3. Create a view to render your todo list items. This view will include a template for the HTML, and a render function to populate the template with data from the collection.

```javascript
var TodoView = Backbone.View.extend({
    tagName: 'li',
    template: _.template('<h3><%= title %></h3><p><%= description %></p>'),
    render: function(){
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});
```

4. Create an instance of your collection, and add some todo list items to it.

```javascript
var todoList = new TodoList();
todoList.add([
    { title: 'Mow the lawn', description: 'Fill the gasoline tank and start the engine' },
    { title: 'Wash the car', description: 'Fill the soap tank and start the engine' }
]);
```

5. Create a view for the entire todo list. This view will loop through the collection, creating a new instance of the TodoView for each item.

```javascript
var TodoListView = Backbone.View.extend({
    tagName: 'ul',
    render: function(){
        this.collection.each(function(todo){
            var todoView = new TodoView({ model: todo });
            this.$el.append(todoView.render().el);
        }, this);
        return this;
    }
});
```

6. Finally, create an instance of the TodoListView, and render it to the page.

```javascript
var todoListView = new TodoListView({ collection: todoList });
$('body').append(todoListView.render().el);
```

This will render an unordered list of your todo list items to the page.

## Helpful links
- [Backbone.js Documentation](http://backbonejs.org/)
- [Creating a Todo List Application with Backbone.js](https://www.taniarascia.com/javascript-mvc-todo-app/)

onelinerhub: [How do I create a todo list application using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-create-a-todo-list-application-using-backbone-js)