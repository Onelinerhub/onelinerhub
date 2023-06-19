# How do I pass a collection to a Backbone.js view?
// plain

You can pass a collection to a Backbone.js view by using the `collection` property. This property should be set to an instance of a Backbone.Collection.

For example, if you have a collection of books you can pass it to a view like this:

```javascript
var books = new Backbone.Collection([
  { title: 'Alice in Wonderland' },
  { title: 'The Hobbit' }
]);

var booksView = new Backbone.View({
  el: '#books',
  collection: books
});
```

In this example, `books` is an instance of a Backbone.Collection and `booksView` is an instance of a Backbone.View. The `collection` property of the view is set to the `books` collection.

You can also pass a collection to a view when creating it, like this:

```javascript
var booksView = new Backbone.View({
  el: '#books',
  collection: new Backbone.Collection([
    { title: 'Alice in Wonderland' },
    { title: 'The Hobbit' }
  ])
});
```

The view will now have access to the collection via the `collection` property.

For more information, see the [Backbone.js documentation](http://backbonejs.org/#View-constructor).

onelinerhub: [How do I pass a collection to a Backbone.js view?](https://onelinerhub.com/backbone.js/how-do-i-pass-a-collection-to-a-backbone-js-view)