# How do I use a template engine with Backbone.js?
// plain

Backbone.js can be used with a template engine to render dynamic HTML content. A template engine is a library that provides a template language for constructing HTML pages.

To use a template engine with Backbone.js, you will need to include the template engine library in your project, and then create a template in the template language. Then, you can use the `Backbone.View.prototype.render` function to render the template with the data from the model.

For example, if you were using the Underscore.js template engine, you could create a template like this:

```
<div>
  <h1><%= title %></h1>
  <p><%= description %></p>
</div>
```

Then, you could render the template using the `render` function:

```javascript
var model = {title: 'Hello World', description: 'This is a description.'};

var template = _.template(templateString);
var html = template(model);

this.$el.html(html);
```

This code would render the following HTML:

```
<div>
  <h1>Hello World</h1>
  <p>This is a description.</p>
</div>
```

## Helpful links

- [Underscore.js Template Documentation](http://underscorejs.org/#template)
- [Backbone.View.prototype.render Documentation](http://backbonejs.org/#View-render)

onelinerhub: [How do I use a template engine with Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-use-a-template-engine-with-backbone-js)