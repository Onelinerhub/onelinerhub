# How can I iterate over a collection in Backbone.js?
// plain

Backbone.js provides several methods for iterating over collections, including the `each()` method. The `each()` method is used to loop through each model in a collection. It takes a callback function as an argument, which is passed two arguments: the model and its index. Here is an example of the `each()` method:

```
var myCollection = new Backbone.Collection([
    {name: 'John'},
    {name: 'Mary'},
    {name: 'Joe'}
]);

myCollection.each(function(model, index) {
    console.log(model.get('name'));
});

// Output:
// John
// Mary
// Joe
```

The `each()` method is useful for iterating over a collection and performing operations on each model. It is also possible to use the `forEach()` and `forIn()` methods for iterating over collections.

The `forEach()` method is similar to the `each()` method, but it does not pass the model index as an argument. Here is an example of the `forEach()` method:

```
var myCollection = new Backbone.Collection([
    {name: 'John'},
    {name: 'Mary'},
    {name: 'Joe'}
]);

myCollection.forEach(function(model) {
    console.log(model.get('name'));
});

// Output:
// John
// Mary
// Joe
```

The `forIn()` method is used to loop through the properties of an object. Here is an example of the `forIn()` method:

```
var myCollection = new Backbone.Collection([
    {name: 'John'},
    {name: 'Mary'},
    {name: 'Joe'}
]);

for (var key in myCollection.models) {
    console.log(myCollection.models[key].get('name'));
}

// Output:
// John
// Mary
// Joe
```

In summary, Backbone.js provides several methods for iterating over collections, including the `each()`, `forEach()`, and `forIn()` methods.

## Helpful links
- [Backbone.Collection.each()](http://backbonejs.org/#Collection-each)
- [Backbone.Collection.forEach()](http://backbonejs.org/#Collection-forEach)
- [Backbone.Collection.forIn()](http://backbonejs.org/#Collection-forIn)

onelinerhub: [How can I iterate over a collection in Backbone.js?](https://onelinerhub.com/backbone.js/how-can-i-iterate-over-a-collection-in-backbone-js)