# How do I get the value of an input field using jQuery?
// plain

To get the value of an input field using jQuery, you can use the `val()` method. This method is used to get the values of form elements such as input, select, textarea.

## Example code

```
<form>
  <input type="text" name="name" id="name" value="John Doe" />
</form>

<script>
  var name = $("#name").val();
  console.log(name);
</script>
```

## Output example

```
John Doe
```

The code above consists of the following parts:
1. An HTML form element with an input field
2. A jQuery script to get the value of the input field

The HTML form element defines the input field with an `id` of `name`. The jQuery script uses the `$("#name")` selector to target the input field and the `val()` method to get its value. The value is then stored in the `name` variable and logged to the console.

## Helpful links
- [jQuery val() method](https://api.jquery.com/val/)

onelinerhub: [How do I get the value of an input field using jQuery?](https://onelinerhub.com/jquery/how-do-i-get-the-value-of-an-input-field-using-jquery)