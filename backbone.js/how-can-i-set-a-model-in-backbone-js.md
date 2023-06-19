# How can I set a model in Backbone.js?
// plain

Setting a model in Backbone.js is a simple process. To begin, you must first create a model object. This is done by extending the Backbone.Model class. For example:

```
var MyModel = Backbone.Model.extend({
    defaults: {
        name: '',
        age: 0
    }
});
```

Once you have a model object, you can create an instance of the model by using the `new` keyword. The following example creates a new instance of the MyModel object:

```
var myModel = new MyModel();
```

You can then set attributes on the model instance using the `set` method. This takes an object containing the attributes and their values. The following example sets the `name` and `age` attributes on the `myModel` instance:

```
myModel.set({
    name: 'John Doe',
    age: 20
});
```

Finally, you can retrieve the attributes from the model instance using the `get` method. This takes the name of the attribute you want to retrieve. The following example retrieves the `name` attribute from the `myModel` instance:

```
var name = myModel.get('name');
// Output: 'John Doe'
```

The `set` and `get` methods are the primary way to interact with a Backbone.js model.

## Helpful links
- [Backbone.js Documentation](http://backbonejs.org/#Model)
- [MDN: Using Object.create()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

onelinerhub: [How can I set a model in Backbone.js?](https://onelinerhub.com/backbone.js/how-can-i-set-a-model-in-backbone-js)