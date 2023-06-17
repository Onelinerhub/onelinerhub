# How do I use jQuery MaskedInput to format user input?
// plain

jQuery MaskedInput is a plugin that allows you to add a mask to an input field to format the user’s input. It is a very useful tool for making sure that user input is in the correct format.

To use jQuery MaskedInput, you first need to include the plugin's JavaScript file.

```
<script src="jquery.maskedinput.js"></script>
```

Then you can call the `mask` function on the input field to define the mask. The mask is a string that defines which characters are accepted and where they should appear.

```
$("#inputField").mask("(999) 999-9999");
```

The mask in the example above defines that the input should consist of three digits, followed by a space, followed by three digits, followed by a dash, followed by four digits.

You can also define custom placeholder characters for the mask.

```
$("#inputField").mask("(999) 999-9999", {placeholder: "X"});
```

In the example above, the placeholder character is set to `X`. This means that the input field will be pre-filled with `X`s, and the user will have to replace them with the correct digits.

For more information about jQuery MaskedInput and how to use it, please refer to the [documentation](https://igorescobar.github.io/jQuery-Mask-Plugin/).

onelinerhub: [How do I use jQuery MaskedInput to format user input?](https://onelinerhub.com/jquery/how-do-i-use-jquery-maskedinput-to-format-user-input)