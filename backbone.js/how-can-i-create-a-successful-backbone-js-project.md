# How can I create a successful Backbone.js project?
// plain

1. Begin by setting up a project folder and creating a file structure that will be easy to maintain and update.
2. Set up the HTML page that will host the Backbone application. Include the necessary libraries, such as jQuery, Underscore, and Backbone.
```
<script src="jquery.js"></script>
<script src="underscore.js"></script>
<script src="backbone.js"></script>
```
3. Create a model that will define the data structure of the application.
```
var User = Backbone.Model.extend({
  defaults: {
    name: '',
    age: 0
  }
});
```
4. Create a collection to store the models.
```
var Users = Backbone.Collection.extend({
  model: User
});
```
5. Create a view that will render the data from the models.
```
var UserView = Backbone.View.extend({
  tagName: 'li',
  render: function(){
    this.$el.html( this.model.get('name') + '(' + this.model.get('age') + ')');
    return this;
  }
});
```
6. Create a router to handle navigation and page navigation.
```
var AppRouter = Backbone.Router.extend({
  routes: {
    '': 'home'
  },
  home: function(){
    // render home page
  }
});
```
7. Finally, create an instance of the router and start Backbone's history.
```
var appRouter = new AppRouter();
Backbone.history.start();
```

## Helpful links
- [Backbone.js Documentation](http://backbonejs.org/)
- [Getting Started with Backbone.js](https://scotch.io/tutorials/getting-started-with-backbone-js)

onelinerhub: [How can I create a successful Backbone.js project?](https://onelinerhub.com/backbone.js/how-can-i-create-a-successful-backbone-js-project)