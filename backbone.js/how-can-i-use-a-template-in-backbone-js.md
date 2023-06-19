# How can I use a template in Backbone.js?
// plain

Backbone.js provides a powerful way to use templates in your application. Templates are used to generate HTML from your model data.

To use a template in Backbone.js, you need to first create a template using a templating language like Underscore.js. For example, the following template creates a list of items from a model:

```
<ul>
  <% _.each(items, function(item) { %>
    <li><%= item.name %></li>
  <% }); %>
</ul>
```

Once the template is created, you can use the `Backbone.View` object to render the template. The `render()` method of the `View` object takes the model data and passes it to the template. For example:

```
var view = new Backbone.View({
  model: items
});

view.render = function() {
  this.$el.html(this.template(this.model.toJSON()));
  return this;
};
```

The `render()` method takes the model data as an argument and passes it to the template. The template is then rendered to the `$el` property of the view.

You can also use a pre-compiled template, which is a template that has already been compiled into JavaScript code. This can be done using a templating library like Handlebars.js.

Finally, you can also use a template engine such as Mustache.js to create and render templates in Backbone.js.

## Code explanation


1. `<ul>` - This is the start tag for an unordered list.
2. `<% _.each(items, function(item) { %>` - This is an Underscore.js loop that iterates through the items in the model and creates a list item for each item.
3. `<li><%= item.name %></li>` - This is a list item tag that displays the item's name.
4. `<% }); %>` - This is the end tag for the Underscore.js loop.
5. `var view = new Backbone.View({` - This creates a new Backbone.View object.
6. `model: items` - This sets the model data for the view.
7. `view.render = function() {` - This is the render() method for the view.
8. `this.$el.html(this.template(this.model.toJSON()));` - This takes the model data and passes it to the template.
9. `return this;` - This returns the view object.

## Helpful links

- [Backbone.js Documentation](http://backbonejs.org/)
- [Underscore.js Documentation](http://underscorejs.org/)
- [Handlebars.js Documentation](http://handlebarsjs.com/)
- [Mustache.js Documentation](http://mustache.github.io/)

onelinerhub: [How can I use a template in Backbone.js?](https://onelinerhub.com/backbone.js/how-can-i-use-a-template-in-backbone-js)