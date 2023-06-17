# How do I use jQuery UI Sortable to arrange elements on a webpage?
// plain

jQuery UI Sortable is a jQuery plugin that allows users to rearrange elements on a webpage by dragging and dropping them. To use it, you must include the jQuery and jQuery UI libraries in your HTML file:

```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
```

You must also specify the `sortable()` method on the jQuery object you wish to sort. For example, to make a list of items sortable:

```
$('#myList').sortable();
```

The `sortable()` method takes a number of options to customize the sortable behavior. For example, you can specify the `axis` option to restrict sorting to either the x-axis or y-axis:

```
$('#myList').sortable({axis: 'y'});
```

You can also specify the `handle` option to specify which elements can be used to drag and drop the items:

```
$('#myList').sortable({handle: '.my-handle'});
```

Finally, you can specify callback functions to be executed when the user starts, stops, or changes the order of the elements. For example, to log the new order of the elements to the console when the user changes the order:

```
$('#myList').sortable({
  change: function( event, ui ) {
    console.log($(this).sortable('toArray'));
  }
});
```

The output of the above code would be an array of the elements in the new order.

## Helpful links
- [jQuery UI Sortable Documentation](https://api.jqueryui.com/sortable/)
- [jQuery Sortable Tutorial](https://jqueryui.com/sortable/)

onelinerhub: [How do I use jQuery UI Sortable to arrange elements on a webpage?](https://onelinerhub.com/jquery/how-do-i-use-jquery-ui-sortable-to-arrange-elements-on-a-webpage)