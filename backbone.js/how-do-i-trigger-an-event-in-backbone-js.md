# How do I trigger an event in Backbone.js?
// plain

Backbone.js provides a way to trigger events when certain conditions are met. To trigger an event, you need to call the trigger() method on a Backbone.Events object.

For example, to trigger an event when a button is clicked, you can use the following code:

```
var button = document.getElementById('button');
button.onclick = function(){
  Backbone.Events.trigger('buttonClicked');
}
```

This will trigger an event called 'buttonClicked' when the button is clicked.

You can also pass arguments to the trigger() method, which will be passed to the event handler. For example:

```
var button = document.getElementById('button');
button.onclick = function(){
  Backbone.Events.trigger('buttonClicked', {data: 'some data'});
}
```

This will trigger an event called 'buttonClicked' with the argument {data: 'some data'}.

You can also listen for events using the on() method, which takes the event name and a callback function as arguments. For example:

```
Backbone.Events.on('buttonClicked', function(data){
  console.log(data); // {data: 'some data'}
});
```

This will call the callback function when the 'buttonClicked' event is triggered, passing the argument provided to the trigger() method.

## Helpful links

- [Backbone.Events](http://backbonejs.org/#Events)
- [trigger()](http://backbonejs.org/#Events-trigger)
- [on()](http://backbonejs.org/#Events-on)

onelinerhub: [How do I trigger an event in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-trigger-an-event-in-backbone-js)