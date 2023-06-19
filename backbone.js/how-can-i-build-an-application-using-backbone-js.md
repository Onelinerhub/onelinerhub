# How can I build an application using Backbone.js?
// plain

Backbone.js is a JavaScript library that makes it easier to create dynamic, single-page web applications. It provides an MVC (Model View Controller) framework that helps to organize code and keep it modular. To build an application using Backbone.js, you need to include the library in your HTML page and create models, views, and controllers.

## Example code

```
<script src="backbone.js"></script>

// Model
var Person = Backbone.Model.extend({
    defaults: {
        name: '',
        age: 0
    }
});

// View
var PersonView = Backbone.View.extend({
    tagName: 'li',
    render: function() {
        this.$el.html(this.model.get('name') + ' (' + this.model.get('age') + ')');
        return this;
    }
});

// Controller
var PeopleController = Backbone.Router.extend({
    routes: {
        "people/:name": "showPerson"
    },
    showPerson: function(name) {
        var person = new Person({name: name, age: 30});
        var personView = new PersonView({model: person});
        $('#people').html(personView.render().el);
    }
});

var peopleController = new PeopleController();
Backbone.history.start();
```

This code creates a `Person` model, a `PersonView` view, and a `PeopleController` router. The `Person` model has two properties, `name` and `age`, and the `PersonView` view renders the model in an HTML `li` element. The `PeopleController` router has a single route, `people/:name`, which will render the `PersonView` with the name specified in the route. Finally, the `Backbone.history.start()` call enables the router.

## Code explanation


1. Include the Backbone.js library in the HTML page: `<script src="backbone.js"></script>`
2. Create a model: `var Person = Backbone.Model.extend({...});`
3. Create a view: `var PersonView = Backbone.View.extend({...});`
4. Create a controller: `var PeopleController = Backbone.Router.extend({...});`
5. Create a route in the controller: `routes: { "people/:name": "showPerson" }`
6. Create a controller action: `showPerson: function(name) {...}`
7. Start the router: `Backbone.history.start();`

## Helpful links

- [Backbone.js](http://backbonejs.org/)
- [Backbone Tutorials](http://backbonetutorials.com/)
- [Getting Started with Backbone.js](https://scotch.io/tutorials/getting-started-with-backbone-js)

onelinerhub: [How can I build an application using Backbone.js?](https://onelinerhub.com/backbone.js/how-can-i-build-an-application-using-backbone-js)