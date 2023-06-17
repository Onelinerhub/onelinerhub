# How do I disable a button using jQuery?
// plain

To disable a button using jQuery, you can use the `prop()` method. This method sets the property of the button to disabled, which will prevent it from being clicked.

## Example code

```javascript
$("button").prop("disabled", true);
```

The code above will disable all buttons on the page.

## Code explanation

- `$("button")`: This is the jQuery selector for all buttons on the page.
- `prop()`: This is the method used to set a property.
- `"disabled"`: This is the property that will be set.
- `true`: This is the value that will be set for the property.

## Helpful links
- [jQuery prop() Documentation](https://api.jquery.com/prop/)

onelinerhub: [How do I disable a button using jQuery?](https://onelinerhub.com/jquery/how-do-i-disable-a-button-using-jquery-1687015584)