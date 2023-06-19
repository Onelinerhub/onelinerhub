# How can I find an example of Backbone.js code on GitHub?
// plain

To find an example of Backbone.js code on GitHub, you can use the GitHub search function.

For example, you can enter the following query into the search bar: `language:javascript backbone`. This will return a list of JavaScript files that use Backbone.js.

Here is an example code block that uses Backbone.js:
```
var User = Backbone.Model.extend({
  defaults: {
    name: 'Guest User',
    age: 23
  },
  validate: function(attrs){
    if (attrs.age < 0) {
      return 'Age must be positive.';
    }
  }
});

var user = new User({name: 'John', age: -1});
user.on("invalid", function(model, error){
  console.log(error);
});
user.save();
```

The output of the example code is:
```
Age must be positive.
```

The code consists of the following parts:
* `var User = Backbone.Model.extend({...})` - this creates a new model class called User.
* `defaults` - this sets default values for the model's attributes.
* `validate` - this sets up a validation function that will be called when the model is saved.
* `var user = new User({name: 'John', age: -1});` - this creates a new instance of the User model with the specified attributes.
* `user.on("invalid", function(model, error){...})` - this sets up a listener that will be called if the model fails validation.
* `user.save()` - this saves the model and triggers the validation function.

Here are some ## Helpful links
* [Backbone.js Documentation](http://backbonejs.org/)
* [GitHub Search](https://github.com/search)

onelinerhub: [How can I find an example of Backbone.js code on GitHub?](https://onelinerhub.com/backbone.js/how-can-i-find-an-example-of-backbone-js-code-on-github)