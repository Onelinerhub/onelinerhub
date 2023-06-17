# How do I create a jQuery accordion?
// plain

To create a jQuery accordion, you need to use the following code:

```
$(function() {
    $( "#accordion" ).accordion();
});
```

## Code explanation


1. `$( "#accordion" )` - This is the selector for the accordion. This can be used to select the element to which the accordion will be applied.
2. `accordion()` - This is the function that will create the accordion.
3. `active` - This is an optional parameter that can be used to specify which accordion panel should be open by default.
4. `collapsible` - This is an optional parameter that can be used to specify whether the accordion panels can be closed.

Here is an example of a customized accordion:

```
$(function() {
    $( "#accordion" ).accordion({
        active: 0,
        collapsible: true
    });
});
```

This code will create an accordion with the id of "accordion", with the first panel open by default, and all panels being able to be closed.

For more information on how to create a jQuery accordion, see the [jQuery UI Accordion documentation](https://api.jqueryui.com/accordion/).

onelinerhub: [How do I create a jQuery accordion?](https://onelinerhub.com/jquery/how-do-i-create-a-jquery-accordion)