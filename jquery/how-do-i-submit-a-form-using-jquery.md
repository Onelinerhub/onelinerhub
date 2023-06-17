# How do I submit a form using jQuery?
// plain

The following example shows how to submit a form using jQuery. The example code will submit the form when the user clicks on the submit button:

```
$('#submit-form').on('click', function() {
  $('#form-id').submit();
});
```

This code works by binding a click event to the submit-form element. When the user clicks on the submit-form element, the form-id form is submitted.

The code consists of the following parts:

1. `$('#submit-form')` - This is a jQuery selector that selects the element with the id of submit-form
2. `.on('click', function() {` - This binds a click event to the submit-form element
3. `$('#form-id')` - This is a jQuery selector that selects the element with the id of form-id
4. `.submit()` - This submits the form-id form

For more information, see the [jQuery documentation](https://api.jquery.com/submit/).

onelinerhub: [How do I submit a form using jQuery?](https://onelinerhub.com/jquery/how-do-i-submit-a-form-using-jquery)