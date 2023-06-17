# How do I use the jQuery UI Datepicker?
// plain

The jQuery UI Datepicker is a popular and widely used plugin that allows users to select a date from an interactive calendar. To use the Datepicker, you must include the jQuery UI library and its associated CSS file on your webpage:

```
<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
```

Then, you can initialize the Datepicker using the `datepicker()` method on a jQuery selection. The following example will create a Datepicker on the `#datepicker` element:

```
$( "#datepicker" ).datepicker();
```

The Datepicker can be customized using a range of options, methods, and events. These include:

- `minDate` and `maxDate`: set the minimum and maximum selectable dates.
- `dateFormat`: set the format of the returned date string.
- `onSelect`: a callback function that is triggered when a date is selected.
- `hide` and `show`: methods that can be used to hide and show the Datepicker.

For more information, see the [jQuery UI Datepicker documentation](https://jqueryui.com/datepicker/).

onelinerhub: [How do I use the jQuery UI Datepicker?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-ui-datepicker)