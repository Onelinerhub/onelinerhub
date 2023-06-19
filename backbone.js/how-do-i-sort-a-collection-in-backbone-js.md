# How do I sort a collection in Backbone.js?
// plain

Backbone.js provides a `sort()` method to sort a collection. This method takes a comparator function as an argument, which is used to compare two models in a collection. The comparator function should return a negative number if the first model should come before the second, a positive number if the first model should come after the second, and 0 if they are equal.

For example, to sort a collection of models by their `name` attribute, we could do the following:

```javascript
var sortedCollection = collection.sort(function(model1, model2) {
  if (model1.get('name') < model2.get('name')) return -1;
  if (model1.get('name') > model2.get('name')) return 1;
  return 0;
});
```

This example code would return a new sorted collection, leaving the original collection unchanged.

## Code explanation


- `collection.sort(function(model1, model2)`: This invokes the `sort()` method on the collection, passing in a comparator function as an argument.
- `model1.get('name')` and `model2.get('name')`: These lines get the `name` attribute from each model in the collection.
- `if (model1.get('name') < model2.get('name')) return -1;`: This line compares the `name` attributes of the two models, returning -1 if the first model should come before the second.
- `if (model1.get('name') > model2.get('name')) return 1;`: This line compares the `name` attributes of the two models, returning 1 if the first model should come after the second.
- `return 0;`: This line returns 0 if the two models are equal.

## Helpful links

- [Backbone.Collection.sort](http://backbonejs.org/#Collection-sort)

onelinerhub: [How do I sort a collection in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-sort-a-collection-in-backbone-js)