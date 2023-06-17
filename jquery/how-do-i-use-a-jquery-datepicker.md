# How do I use a jQuery datepicker?
// plain

To use a jQuery datepicker, you must include the jQuery library and the jQuery UI library. In addition, you must include a CSS file for the datepicker's styling.

To create a datepicker, you must first create an HTML element to attach the datepicker to. This can be a `<input>` or a `<div>` element.

Then, you must call the `datepicker()` function on the element.

For example:
```
<input type="text" id="datepicker">
<script>
$( "#datepicker" ).datepicker();
</script>
```

This will create a datepicker element on the page. You can also add options to the `datepicker()` function to customize the datepicker. For example:
```
$( "#datepicker" ).datepicker({
    showButtonPanel: true,
    changeMonth: true,
    changeYear: true
});
```

This will add a button panel, and allow the user to change the month and year.

You can find more information and examples of using jQuery datepicker on the [jQuery UI website](https://jqueryui.com/datepicker/).

onelinerhub: [How do I use a jQuery datepicker?](https://onelinerhub.com/jquery/how-do-i-use-a-jquery-datepicker)