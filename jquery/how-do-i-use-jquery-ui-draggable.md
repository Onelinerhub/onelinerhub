# How do I use jQuery UI draggable?
// plain

To use jQuery UI draggable, you first need to include the jQuery UI library in your HTML page. You can do this by adding the following code to the <head> section of your HTML page:

```
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js" integrity="sha256-VazP97ZCwtekAsvgPBSUwPFKdrwD3unUfSGVYrahUqU=" crossorigin="anonymous"></script>
```

Next, you need to add the `draggable()` function to the element you want to make draggable. For example, if you want to make a `<div>` element draggable, you can use the following code:

```
$("#myDiv").draggable();
```

You can also customize the draggable behavior by passing in an options object. For example, the following code will make the element snap to a grid with 10px increments:

```
$("#myDiv").draggable({
  grid: [ 10, 10 ]
});
```

You can also specify functions to be called when the draggable element is dragged, started, stopped, or reverted. For example, the following code will display an alert when the draggable element is started:

```
$("#myDiv").draggable({
  start: function(event, ui) {
    alert("Drag started!");
  }
});
```

You can find more information about the `draggable()` function and its options in the [jQuery UI documentation](https://api.jqueryui.com/draggable/).

## Code explanation
**

1. Include jQuery UI library in HTML page: `<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js" integrity="sha256-VazP97ZCwtekAsvgPBSUwPFKdrwD3unUfSGVYrahUqU=" crossorigin="anonymous"></script>`
2. Add `draggable()` function to element you want to make draggable: `$("#myDiv").draggable();`
3. Customize draggable behavior by passing in an options object: `$("#myDiv").draggable({ grid: [ 10, 10 ] });`
4. Specify functions to be called when draggable element is dragged, started, stopped, or reverted: `$("#myDiv").draggable({ start: function(event, ui) { alert("Drag started!"); } });`

**## Helpful links**

- [jQuery UI documentation](https://api.jqueryui.com/draggable/)

onelinerhub: [How do I use jQuery UI draggable?](https://onelinerhub.com/jquery/how-do-i-use-jquery-ui-draggable)