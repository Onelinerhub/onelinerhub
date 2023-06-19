# How do I determine the length of a collection in Backbone.js?
// plain

To determine the length of a collection in Backbone.js, you can use the `length` property. This property returns the number of models in the collection.

For example:

```
var collection = new Backbone.Collection([
  {name: 'John', age: 28},
  {name: 'Jack', age: 30}
]);

console.log(collection.length);
// Output: 2
```

The code above creates a new Backbone Collection with two models. The `length` property returns the number of models in the collection, which in this case is 2.

The following list contains the parts of the code above with an explanation of each part:
- `var collection = new Backbone.Collection([`: Creates a new Backbone Collection.
- `{name: 'John', age: 28},`: Creates a model with the properties `name` and `age`.
- `{name: 'Jack', age: 30}`: Creates another model with the properties `name` and `age`.
- `]);`: Closes the array of models.
- `console.log(collection.length);`: Logs the length of the collection to the console.
- `// Output: 2`: The output of the code.

## Helpful links
- [Backbone.Collection](http://backbonejs.org/#Collection)

onelinerhub: [How do I determine the length of a collection in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-determine-the-length-of-a-collection-in-backbone-js)