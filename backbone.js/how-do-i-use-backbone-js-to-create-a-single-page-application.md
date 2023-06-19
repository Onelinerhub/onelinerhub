# How do I use Backbone.js to create a single page application?
// plain

Backbone.js is a JavaScript library that can be used to create single page applications (SPAs). It is based on the Model-View-Presenter (MVP) design pattern, which allows for a separation of data, view, and business logic.

To use Backbone.js to create an SPA, you will need to create a model, a view, and a presenter. The model is responsible for managing the application's data, the view is responsible for displaying the data, and the presenter is responsible for handling user interactions and updating the model and view.

## Example code

```
// Model
var User = Backbone.Model.extend({
  defaults: {
    name: '',
    age: 0
  }
});

// View
var UserView = Backbone.View.extend({
  template: _.template('<h1><%= name %></h1><p><%= age %></p>'),
  render: function(){
    this.$el.html(this.template(this.model.attributes));
    return this;
  }
});

// Presenter
var UserPresenter = Backbone.View.extend({
  events: {
    'click #update': 'update'
  },
  update: function(){
    this.model.set('name', $('#name').val());
    this.model.set('age', $('#age').val());
    this.view.render();
  }
});

// Create instance of model
var user = new User({name: 'John', age: 30});

// Create instance of view
var userView = new UserView({model: user});

// Create instance of presenter
var userPresenter = new UserPresenter({model: user, view: userView});

// Render view
userView.render();

// Output
<h1>John</h1><p>30</p>
```

Parts of the code:
- Model: The `User` model is responsible for managing the application's data. It is a Backbone.Model and has two default attributes, `name` and `age`.
- View: The `UserView` view is responsible for displaying the data. It is a Backbone.View and has a template and a render function.
- Presenter: The `UserPresenter` presenter is responsible for handling user interactions and updating the model and view. It is a Backbone.View and has an `update` event handler.

## Helpful links
- Backbone.js Documentation: http://backbonejs.org/
- Model-View-Presenter Design Pattern: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter

onelinerhub: [How do I use Backbone.js to create a single page application?](https://onelinerhub.com/backbone.js/how-do-i-use-backbone-js-to-create-a-single-page-application)