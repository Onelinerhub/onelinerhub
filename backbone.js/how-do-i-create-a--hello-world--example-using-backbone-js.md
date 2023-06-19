# How do I create a "Hello World" example using Backbone.js?
// plain

Creating a "Hello World" example using Backbone.js is quite simple.

1. Create an HTML page with the following code:

```
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.1/underscore-min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.3.3/backbone-min.js"></script>
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>
```

2. Create a script tag in the HTML page and add the following code:

```
<script>
  var AppView = Backbone.View.extend({
    el: '#app',
    render: function(){
      this.$el.html("Hello World!");
    }
  });

  var appView = new AppView();
  appView.render();
</script>
```

This code will create a view and attach it to the HTML element with the ID of `app`. The view will then render the text "Hello World!" into that element.

The output of this code will be the text "Hello World!" rendered on the page.

## Helpful links
- https://backbonejs.org/
- https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics

onelinerhub: [How do I create a "Hello World" example using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-create-a--hello-world--example-using-backbone-js)