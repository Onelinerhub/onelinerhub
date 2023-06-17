# How do I use jQuery UI Dialog?
// plain

### jQuery UI Dialog

jQuery UI Dialog is a UI component that can be used to display information or request input from a user. It is a modal window that can be used to prompt the user for information or display a message.

The following example code will create a simple dialog box with a message and an "OK" button:
```javascript
$( "#dialog" ).dialog({
    autoOpen: false,
    show: {
        effect: "blind",
        duration: 1000
    },
    hide: {
        effect: "explode",
        duration: 1000
    }
});

$( "#opener" ).click(function() {
    $( "#dialog" ).dialog( "open" );
});
```

The code is composed of the following parts:

1. `$( "#dialog" ).dialog({ ... })`: This creates the dialog box. The options inside the brackets are used to customize the dialog box.

2. `$( "#opener" ).click(function() { ... })`: This binds a click event to the element with the id "opener". When this element is clicked, the dialog box will open.

3. `$( "#dialog" ).dialog( "open" )`: This opens the dialog box.

For more information, see the [jQuery UI Dialog documentation](https://api.jqueryui.com/dialog/).

onelinerhub: [How do I use jQuery UI Dialog?](https://onelinerhub.com/jquery/how-do-i-use-jquery-ui-dialog)