# How can I override a method using Backbone.js?
// plain

Backbone.js allows you to override a method by using the `extend` method. The `extend` method takes two parameters: the first parameter is the object that contains the new methods, and the second parameter is the object that contains the existing methods.

For example, if you wanted to override the `fetch` method of a Backbone Model, you could do the following:

```javascript
var MyModel = Backbone.Model.extend({
  fetch: function(){
    console.log('fetching data...');
  }
});
```

This would override the `fetch` method of the Backbone Model with the new `fetch` method defined above. The output of this code would be:

```
fetching data...
```

## Code explanation


- `var MyModel` - creates a variable to store the new model
- `Backbone.Model.extend` - extends the Backbone Model with a new method
- `fetch` - the new `fetch` method to override the existing one
- `console.log` - logs a message to the console

## Helpful links

- [Backbone.js Documentation](http://backbonejs.org/)
- [Backbone.js API Reference](http://backbonejs.org/#Model)

onelinerhub: [How can I override a method using Backbone.js?](https://onelinerhub.com/backbone.js/how-can-i-override-a-method-using-backbone-js)