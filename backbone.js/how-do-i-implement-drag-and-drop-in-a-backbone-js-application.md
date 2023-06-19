# How do I implement drag and drop in a Backbone.js application?
// plain

To implement drag and drop in a Backbone.js application, we need to use the jQuery UI library. This library provides a set of functions to allow us to easily add drag and drop functionality to our application.

First, we need to include the jQuery UI library in our application. We can do this by adding the following line of code to our HTML page:
```html
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>
```

Next, we need to add the draggable() function to the element we want to be draggable. This is done by adding the following code to our JavaScript file:
```javascript
$( "#draggable" ).draggable();
```

We can also add an event listener to the draggable element. This will allow us to execute a function when the element is dragged. For example, we can add the following code to our JavaScript file:
```javascript
$( "#draggable" ).on( "drag", function( event, ui ) {
  console.log( "Element was dragged!" );
});
```

Finally, we can add the droppable() function to the element we want to be a drop target. This is done by adding the following code to our JavaScript file:
```javascript
$( "#droppable" ).droppable({
  drop: function( event, ui ) {
    console.log( "Element was dropped!" );
  }
});
```

The above code will allow us to implement drag and drop functionality in a Backbone.js application.

Parts of the code:

- `<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>`: This line of code is used to include the jQuery UI library in our application.

- `$( "#draggable" ).draggable();`: This line of code is used to add the draggable() function to the element we want to be draggable.

- `$( "#draggable" ).on( "drag", function( event, ui ) {`: This line of code is used to add an event listener to the draggable element.

- `$( "#droppable" ).droppable({`: This line of code is used to add the droppable() function to the element we want to be a drop target.

## Helpful links
- [jQuery UI](https://jqueryui.com/)
- [Backbone.js](http://backbonejs.org/)

onelinerhub: [How do I implement drag and drop in a Backbone.js application?](https://onelinerhub.com/backbone.js/how-do-i-implement-drag-and-drop-in-a-backbone-js-application)