# How do I learn the basics of Backbone.js?
// plain

1. Read the official documentation of Backbone.js. It contains a lot of information about the basics of the framework.
2. Learn the Model-View-Controller (MVC) architecture, which Backbone.js follows.
3. Understand the different components of Backbone.js such as Models, Views, Collections, Routers and Events.
4. Learn the basics of the Backbone.js API, such as creating models, views, collections and routers.
5. Get familiar with the Backbone.js events system, which allows you to bind and trigger custom events.
6. Understand the Backbone.js conventions, such as the use of the `sync` method for persisting data.
7. Practice writing code with Backbone.js. Try creating a simple application with models, views and collections.

## Example code

```
// Create a Model
var Person = Backbone.Model.extend({
    defaults: {
        name: '',
        age: 0
    }
});

// Create a Collection
var PeopleCollection = Backbone.Collection.extend({
    model: Person
});

// Create a View
var PeopleView = Backbone.View.extend({
    el: '#people',
    render: function() {
        this.collection.each(function(person) {
            var personView = new PersonView({ model: person });
            this.$el.append(personView.render().el);
        }, this);
        return this;
    }
});

// Instantiate the Collection
var peopleCollection = new PeopleCollection([
    {
        name: 'John',
        age: 20
    },
    {
        name: 'Jane',
        age: 24
    }
]);

// Instantiate the View
var peopleView = new PeopleView({ collection: peopleCollection });
peopleView.render();
```

## Output example

None

onelinerhub: [How do I learn the basics of Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-learn-the-basics-of-backbone-js)