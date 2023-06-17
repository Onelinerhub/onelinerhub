# How do I use jQuery UI Autocomplete?
// plain

jQuery UI Autocomplete is a widget which provides users with a list of suggestions, as they type, from which they can select an item. It is an easy way to enable users to quickly find and select from a list of values as they type.

The following example shows how to use jQuery UI Autocomplete:

```
$(document).ready(function() {
    var availableTags = [
        "ActionScript",
        "AppleScript",
        "Asp",
        "BASIC",
        "C",
        "C++"
    ];
    $( "#tags" ).autocomplete({
        source: availableTags
    });
});
```

This example code will create a textbox with an autocomplete feature. As the user types, a list of suggestions will appear from the `availableTags` array.

## Code explanation


- `$(document).ready(function() {`: This code part ensures that the code is executed after the DOM is fully loaded.

- `var availableTags = [ ... ];`: This code part creates an array of strings which will be used as the source of the autocomplete suggestions.

- `$("#tags").autocomplete({ ... });`: This code part initializes the autocomplete widget and sets the `availableTags` array as the source of the suggestions.

For more information, see the [jQuery UI Autocomplete documentation](https://api.jqueryui.com/autocomplete/).

onelinerhub: [How do I use jQuery UI Autocomplete?](https://onelinerhub.com/jquery/how-do-i-use-jquery-ui-autocomplete)