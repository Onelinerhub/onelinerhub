# How do I initialize a Backbone.js Model?
// plain

A Backbone Model is a basic unit of data that your application will be using. To initialize a Backbone Model, you need to create a new instance of the Model class, passing in an object literal with the desired properties.

```
var myModel = new Backbone.Model({
  property1: 'value1',
  property2: 'value2'
});
```

This creates a new Model instance with two properties, `property1` and `property2`, with the respective values of `value1` and `value2`.

You can also pass in an array of attributes to the constructor, which will be set as properties on the Model:

```
var myModel = new Backbone.Model([
  {property1: 'value1'},
  {property2: 'value2'}
]);
```

The Model constructor also takes an optional `options` parameter, which can be used to define any additional options for the model:

```
var myModel = new Backbone.Model({
  property1: 'value1',
  property2: 'value2'
}, {
  option1: 'optionValue1',
  option2: 'optionValue2'
});
```

Once the Model is initialized, you can access the properties and options using the `get()` method:

```
var property1 = myModel.get('property1'); // returns 'value1'
var option1 = myModel.get('option1'); // returns 'optionValue1'
```

You can also set values on the model using the `set()` method:

```
myModel.set('property1', 'newValue1');
```

## Helpful links
- [Backbone.js Model Documentation](http://backbonejs.org/#Model)
- [Backbone.js Model API Reference](http://backbonejs.org/#Model-constructor)

onelinerhub: [How do I initialize a Backbone.js Model?](https://onelinerhub.com/backbone.js/how-do-i-initialize-a-backbone-js-model)