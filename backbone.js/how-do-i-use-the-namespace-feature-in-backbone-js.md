# How do I use the namespace feature in Backbone.js?
// plain

Backbone.js provides a convenient way to organize application code into namespaces. This is done by creating objects that contain all of the application's code.

To use this feature, you first create an object for your namespace. For example:

```
var App = {};
```

Then, you can add properties and methods to this object. For example:

```
App.Model = {
  init: function(){
    // some code here
  },
  doSomething: function(){
    // some code here
  }
};
```

You can also create sub-namespaces by adding objects to the parent namespace. For example:

```
App.Views = {};
App.Models = {};
App.Collections = {};
```

You can then add properties and methods to these sub-namespaces:

```
App.Views.MyView = {
  init: function(){
    // some code here
  },
  doSomething: function(){
    // some code here
  }
};
```

You can also use the namespace feature to create a single global object for your application. For example:

```
var App = {
  Views: {},
  Models: {},
  Collections: {}
};
```

This allows you to access all of your application code from a single global object.

## Helpful links
- [Backbone.js Namespacing](http://backbonetutorials.com/namespacing/)
- [Organizing Your Code With Backbone.js Namespacing](https://www.sitepoint.com/organizing-your-code-with-backbone-js-namespacing/)

onelinerhub: [How do I use the namespace feature in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-use-the-namespace-feature-in-backbone-js)