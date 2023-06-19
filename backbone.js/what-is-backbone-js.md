# What is Backbone.js?
// plain

Backbone.js is a JavaScript library that provides an MVC framework for building single-page web applications. It is designed to give structure to web applications by providing models with key-value binding and custom events, collections with a rich API of enumerable functions, views with declarative event handling, and connects it all to your existing API over a RESTful JSON interface.

```
var AppView = Backbone.View.extend({
  el: '#container',
  initialize: function(){
    this.render();
  },
  render: function(){
    this.$el.html("Hello World!");
  }
});

var appView = new AppView();
```

## Output example


Hello World!

The code above creates a view with an element attached to it. The `el` property is a reference to the element in the DOM that the view will be attached to. The `initialize` function is called when the view is instantiated and the `render` function is called to render the view.

Parts of the code:

- `var AppView`: This is a variable that is used to create the view.
- `Backbone.View.extend`: This is a method used to extend the Backbone.View prototype.
- `el`: This is a property that is used to reference the element in the DOM that the view will be attached to.
- `initialize`: This is a function that is called when the view is instantiated.
- `render`: This is a function that is used to render the view.

## Helpful links

- [Backbone.js Documentation](http://backbonejs.org/)
- [Backbone Tutorial](http://backbonetutorials.com/)

onelinerhub: [What is Backbone.js?](https://onelinerhub.com/backbone.js/what-is-backbone-js)