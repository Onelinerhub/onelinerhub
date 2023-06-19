# How do I add an onclick event to a Backbone.js element?
// plain

The easiest way to add an onclick event to a Backbone.js element is to use the view's `events` hash. This hash is used to bind DOM events to methods on the view.

For example, if you have a view called `ButtonView`, you could set up the onclick event like so:

```javascript
var ButtonView = Backbone.View.extend({
  events: {
    'click .my-button': 'onButtonClick'
  },
  onButtonClick: function(e) {
    // Do something
  }
});
```

In the above example, the `events` hash binds the `onButtonClick` method to the `click` event of any element with the class `my-button`.

The `onButtonClick` method will be called when the `click` event is triggered, and the click event's data will be passed as the `e` argument.

## Code explanation

- `events` hash: Used to bind DOM events to methods on the view.
- `ButtonView`: The view in which the onclick event is being set up.
- `click .my-button`: The DOM event being bound.
- `onButtonClick`: The method that will be called when the `click` event is triggered.
- `e` argument: The click event's data that will be passed to the `onButtonClick` method.

Here are some ## Helpful links
- [Backbone.View events](http://backbonejs.org/#View-delegateEvents)
- [DOM events](https://developer.mozilla.org/en-US/docs/Web/Events)

onelinerhub: [How do I add an onclick event to a Backbone.js element?](https://onelinerhub.com/backbone.js/how-do-i-add-an-onclick-event-to-a-backbone-js-element)