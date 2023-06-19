# How do I implement a Backbone.js MVC example?
// plain

To implement a Backbone.js MVC example, first create a simple HTML page with a script tag to include the Backbone.js library:

```
<html>
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.3.3/backbone-min.js"></script>
  </head>
  <body>
  </body>
</html>
```

Then, create a basic Model, View, and Collection with the following code blocks:

Model:
```
var UserModel = Backbone.Model.extend({
  defaults: {
    name: '',
    age: 0
  }
});
```

View:
```
var UserView = Backbone.View.extend({
  tagName: 'li',
  render: function() {
    this.$el.html(this.model.get('name') + ' (' + this.model.get('age') + ')');
    return this;
  }
});
```

Collection:
```
var UserCollection = Backbone.Collection.extend({
  model: UserModel
});
```

Finally, instantiate the Model, View, and Collection, and render the View:

```
var user = new UserModel({name: 'John', age: 25});
var userView = new UserView({model: user});
var userCollection = new UserCollection([user]);

$('body').html(userView.render().el);
```

## Output example

```
<li>John (25)</li>
```

## Code explanation

- HTML page to include Backbone.js library
- Model: UserModel
- View: UserView
- Collection: UserCollection
- Instantiation of Model, View, and Collection
- Rendering of View

## Helpful links
- [Backbone.js](http://backbonejs.org/)
- [Backbone.js Model](http://backbonejs.org/#Model)
- [Backbone.js View](http://backbonejs.org/#View)
- [Backbone.js Collection](http://backbonejs.org/#Collection)

onelinerhub: [How do I implement a Backbone.js MVC example?](https://onelinerhub.com/backbone.js/how-do-i-implement-a-backbone-js-mvc-example)