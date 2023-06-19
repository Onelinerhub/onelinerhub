# How do I use Backbone.js to bind data to my application?
// plain

Backbone.js provides a simple way to bind data to your application. This is done through the use of Models, Views, and Collections.

Models are the core of any Backbone.js application. They represent the data for your application, and can be used to store, retrieve, and sync data with a server. Models are typically created with a set of attributes and methods.

Views are used to control the rendering and events of the application. They act as the interface between the Model and the DOM (Document Object Model). A View can be used to listen for events on the Model and update the UI accordingly.

Collections are used to store and manage a set of Models. They provide a number of useful methods for manipulating the Models, such as sorting, filtering, and fetching data from a server.

## Example code

```
// Create a Model
var Person = Backbone.Model.extend({
    defaults: {
        name: 'John Doe',
        age: 30
    }
});

// Create a View
var PersonView = Backbone.View.extend({
    render: function(){
        this.$el.html(this.model.get('name') + ' (' + this.model.get('age') + ' years old)');
        return this;
    }
});

// Create a Collection
var People = Backbone.Collection.extend({
    model: Person
});

// Instantiate a Collection
var people = new People([
    {
        name: 'John Doe',
        age: 30
    },
    {
        name: 'Jane Doe',
        age: 25
    }
]);

// Instantiate a View, passing in the Model
var personView = new PersonView({ model: people.at(0) });

// Render the View
personView.render();
```

## Output example

```
John Doe (30 years old)
```

## Helpful links
- [Backbone.js Models](http://backbonejs.org/#Model)
- [Backbone.js Views](http://backbonejs.org/#View)
- [Backbone.js Collections](http://backbonejs.org/#Collection)

onelinerhub: [How do I use Backbone.js to bind data to my application?](https://onelinerhub.com/backbone.js/how-do-i-use-backbone-js-to-bind-data-to-my-application)