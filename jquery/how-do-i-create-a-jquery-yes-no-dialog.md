# How do I create a jQuery Yes/No dialog?
// plain

Creating a jQuery Yes/No dialog is a simple process. Following is an example code block to do this:

```
$('#dialog-confirm').dialog({
    autoOpen: false,
    resizable: false,
    height:140,
    modal: true,
    buttons: {
        "Yes": function() {
            $(this).dialog("close");
            //do something
        },
        "No": function() {
            $(this).dialog("close");
            //do something
        }
    }
});
```

This code block will create a Yes/No dialog box with two buttons - Yes and No. When the user clicks on any of these buttons, the dialog box will close and the code inside the corresponding function will be executed.

## Code explanation


1. `$('#dialog-confirm').dialog({` - This initializes the dialog box and all the settings are passed in the form of an object.

2. `autoOpen: false` - This is used to specify whether the dialog box should open automatically or not.

3. `resizable: false` - This is used to specify whether the dialog box should be resizable or not.

4. `height:140` - This is used to specify the height of the dialog box in pixels.

5. `modal: true` - This is used to specify whether the dialog box should be modal or not.

6. `buttons: { ... }` - This is used to specify the buttons that should be displayed in the dialog box.

7. `"Yes": function() { ... }` - This is used to specify the code that should be executed when the user clicks on the Yes button.

8. `"No": function() { ... }` - This is used to specify the code that should be executed when the user clicks on the No button.

9. `$(this).dialog("close")` - This is used to close the dialog box.

## Helpful links
- https://api.jqueryui.com/dialog/
- https://www.tutorialrepublic.com/codelab.php?topic=jquery&file=jquery-ui-dialog-modal-form

onelinerhub: [How do I create a jQuery Yes/No dialog?](https://onelinerhub.com/jquery/how-do-i-create-a-jquery-yes-no-dialog)