# How do I create a Backbone.js collection example?
// plain

Creating a Backbone.js collection example is a straightforward process. The following code block will create a new collection of items called `MyCollection`:
```
var MyCollection = Backbone.Collection.extend({
  url: '/items'
});
```

The code above creates a new collection called `MyCollection` that will fetch its items from the `/items` route.

Now we can create a new instance of `MyCollection` and add some items to it:
```
var myCollection = new MyCollection();
myCollection.add([
  { name: 'Item 1', id: 1 },
  { name: 'Item 2', id: 2 }
]);
```

The code above creates a new instance of `MyCollection` and adds two items to it. We can now access these items using the `myCollection.models` property:

```
console.log(myCollection.models);
// [
//   { name: 'Item 1', id: 1 },
//   { name: 'Item 2', id: 2 }
// ]
```

The output of the code above is an array of the two items added to `myCollection`.

For more information on Backbone.js collections, please refer to the [documentation](http://backbonejs.org/#Collection).

onelinerhub: [How do I create a Backbone.js collection example?](https://onelinerhub.com/backbone.js/how-do-i-create-a-backbone-js-collection-example)