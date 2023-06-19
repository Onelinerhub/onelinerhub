# How do I use a Backbone.js HTML template?
// plain

Using Backbone.js with HTML templates is a great way to create dynamic web applications.

To use an HTML template with Backbone.js, you need to first define the template inside a `<script>` tag:

```html
<script type="text/template" id="my-template">
  <div>
    <h1>My Template</h1>
    <p>Hello, <%= name %></p>
  </div>
</script>
```

Next, you need to create a view in Backbone.js that will use the template:

```javascript
var MyView = Backbone.View.extend({
  template: _.template($('#my-template').html()),
  render: function() {
    this.$el.html(this.template({name: 'World'}));
    return this;
  }
});
```

When the view is rendered, it will use the template and replace the `<%= name %>` placeholder with the value of the `name` property passed to the template. The output of the view will be:

```html
<div>
  <h1>My Template</h1>
  <p>Hello, World</p>
</div>
```

Here are some useful links for further reading:

- [Backbone.js Documentation](https://backbonejs.org/)
- [Underscore.js Documentation](http://underscorejs.org/)
- [Using Underscore.js Templates](http://underscorejs.org/#template)

onelinerhub: [How do I use a Backbone.js HTML template?](https://onelinerhub.com/backbone.js/how-do-i-use-a-backbone-js-html-template)