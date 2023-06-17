# picker

How do I use a jQuery year picker?
// plain

A jQuery year picker is a user interface component that allows a user to select a year from a list of years. It is typically used in forms to select a year for a date field.

To use a jQuery year picker, you need to include the jQuery library and the jQuery UI library in your HTML page.

```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
```

You then need to create an HTML element to contain the year picker. This can be a `<div>` element, or any other element that can contain other elements.

```
<div id="yearpicker"></div>
```

Next, you need to call the `datepicker()` method on the element. This will create the year picker.

```
$( "#yearpicker" ).datepicker({
    changeMonth: false,
    changeYear: true,
    showButtonPanel: true,
    dateFormat: 'yy'
});
```

The code above will create a year picker with the following options:

* `changeMonth`: set to `false` to prevent the user from selecting a month
* `changeYear`: set to `true` to allow the user to select a year
* `showButtonPanel`: set to `true` to show the button panel at the bottom of the year picker
* `dateFormat`: set to `yy` to show the year in the picker

The year picker will look like this:

![Year Picker](https://i.imgur.com/JXU1KcQ.png)

For more information on using jQuery year pickers, see the following links:

* [jQuery UI Datepicker - Year only](https://api.jqueryui.com/datepicker/#option-dateFormat)
* [How to Create a Year Picker with jQuery UI Datepicker](https://www.sitepoint.com/create-year-picker-jquery-ui-datepicker/)

onelinerhub: [picker

How do I use a jQuery year picker?](https://onelinerhub.com/jquery/picker--how-do-i-use-a-jquery-year-picker)