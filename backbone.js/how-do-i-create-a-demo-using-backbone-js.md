# How do I create a demo using Backbone.js?
// plain

To create a demo using Backbone.js, you need to first create a basic HTML page and include the Backbone library.

```
<html>
  <head>
    <script type="text/javascript" src="backbone.js"></script>
  </head>
  <body>
  </body>
</html>
```

Next, you need to create a model, a view, and a collection. The model is used to store data, the view is used to render it, and the collection is used to store multiple models.

```
var Model = Backbone.Model.extend({
  defaults: {
    title: '',
    description: ''
  }
});

var View = Backbone.View.extend({
  render: function(){
    var template = _.template($('#template').html());
    var html = template(this.model.toJSON());
    this.$el.html(html);
  }
});

var Collection = Backbone.Collection.extend({
  model: Model
});
```

Then, you need to create a template to render the data. This template can be written in HTML, JavaScript, or a templating language like Mustache.

```
<script type="text/template" id="template">
  <h1><%= title %></h1>
  <p><%= description %></p>
</script>
```

Finally, you need to create an instance of the model, view, and collection, and render the view.

```
var model = new Model({
  title: 'My Demo',
  description: 'This is a demo of Backbone.js'
});

var view = new View({
  model: model
});

var collection = new Collection([
  model
]);

view.render();
```

This will render the template with the data from the model.

## Helpful links

- [Backbone.js Documentation](http://backbonejs.org/)
- [Getting Started with Backbone.js](https://www.tutorialspoint.com/backbonejs/backbonejs_getting_started.htm)

onelinerhub: [How do I create a demo using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-create-a-demo-using-backbone-js)