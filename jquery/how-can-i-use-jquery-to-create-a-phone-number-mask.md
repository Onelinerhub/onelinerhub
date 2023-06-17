# How can I use jQuery to create a phone number mask?
// plain

To create a phone number mask using jQuery, you can use the `mask` method of the jQuery Mask Plugin. This plugin allows you to specify a mask for input fields that will automatically format user input as they type.

For example, to create a mask for a US phone number, you can use the following code:
```javascript
$('#phone').mask('(000) 000-0000');
```

This code will create a mask for an input field with the id `phone` that will automatically format the user's input as a US phone number.

The code consists of the following parts:
- `$('#phone')` - This is a jQuery selector for the input field with an id of `phone`.
- `mask('(000) 000-0000')` - This is the jQuery Mask Plugin method that specifies the mask for the input field.

Here is a list of ## Helpful links
- [jQuery Mask Plugin](https://igorescobar.github.io/jQuery-Mask-Plugin/)
- [jQuery Selectors](https://api.jquery.com/category/selectors/)

onelinerhub: [How can I use jQuery to create a phone number mask?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-create-a-phone-number-mask)