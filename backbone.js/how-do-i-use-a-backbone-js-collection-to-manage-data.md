# How do I use a Backbone.js collection to manage data?
// plain

A Backbone.js collection is a JavaScript object that can be used to manage data. It provides an API for adding, removing, and fetching models from the collection. Here's an example of how to create a collection and add models to it:

```
var MyCollection = Backbone.Collection.extend({});
var myCollection = new MyCollection();

myCollection.add([
  {name: "John", age: 30},
  {name: "Jane", age: 25},
  {name: "Sam", age: 28}
]);
```

This code will create a new collection called `MyCollection` and add three models to it. The models will have two properties each - `name` and `age`.

You can then access the models in the collection using the `get` method. For example, to get the model with the name "John":

```
var johnModel = myCollection.get("John");
console.log(johnModel.get("age")); // 30
```

You can also use the `each` method to loop through all the models in the collection:

```
myCollection.each(function(model) {
  console.log(model.get("name"));
});

// John
// Jane
// Sam
```

You can find more information about Backbone.js collections in the [official documentation](http://backbonejs.org/#Collection).

onelinerhub: [How do I use a Backbone.js collection to manage data?](https://onelinerhub.com/backbone.js/how-do-i-use-a-backbone-js-collection-to-manage-data)