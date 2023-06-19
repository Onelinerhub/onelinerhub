# How do I create a model in Backbone.js?
// plain

Backbone.js provides an MVC framework for creating models. To create a model, you first need to define a model class using the `Backbone.Model.extend` method. This method takes an object as an argument, which defines the model's attributes and methods.

For example:

```javascript
var Person = Backbone.Model.extend({
  defaults: {
    name: 'John Doe',
    age: 30
  }
});
```

This defines a `Person` model class with two attributes: `name` and `age`.

You can then instantiate a model object from this class like so:

```javascript
var person = new Person();
console.log(person.get('name')); // Outputs 'John Doe'
```

The `person` object now has the attributes `name` and `age` set to the default values defined in the `Person` model class.

You can also set and get the model's attributes using the `set` and `get` methods:

```javascript
person.set('name', 'Jane Doe');
console.log(person.get('name')); // Outputs 'Jane Doe'
```

You can also define custom methods on the model class which can be used to manipulate the model's attributes:

```javascript
var Person = Backbone.Model.extend({
  defaults: {
    name: 'John Doe',
    age: 30
  },
  increaseAge: function(){
    this.set('age', this.get('age') + 1);
  }
});

var person = new Person();
person.increaseAge();
console.log(person.get('age')); // Outputs 31
```

For more information on creating models in Backbone.js, see the [Backbone.js documentation](http://backbonejs.org/#Model).

onelinerhub: [How do I create a model in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-create-a-model-in-backbone-js)