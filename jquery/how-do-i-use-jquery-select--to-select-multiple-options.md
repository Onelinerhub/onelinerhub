# How do I use jQuery Select2 to select multiple options?
// plain

To use jQuery Select2 to select multiple options, you need to use the `multiple` attribute in the `select` tag. The `multiple` attribute allows the user to select more than one option from the dropdown list.

For example:
```
<select id="example" multiple="multiple">
    <option value="1">Option 1</option>
    <option value="2">Option 2</option>
    <option value="3">Option 3</option>
    <option value="4">Option 4</option>
    <option value="5">Option 5</option>
</select>
```

Then, you need to initialize the Select2 plugin by using the following code:
```
$('#example').select2({
    placeholder: 'Select an option',
    multiple: true // allows multiple selection
});
```

After that, you can select multiple options by pressing the `Ctrl` key and clicking on the desired options.

The parts of the code are:
1. `select` tag with `multiple` attribute - defines the select box and allows multiple selection
2. `select2` initialization - initializes the Select2 plugin
3. `Ctrl` key - allows multiple selection

## Helpful links
- [Select2 Documentation](https://select2.org/getting-started/basic-usage)
- [jQuery Select2 - Multiple Select Examples](https://www.phpflow.com/jquery/jquery-select2-multiple-select-examples/)

onelinerhub: [How do I use jQuery Select2 to select multiple options?](https://onelinerhub.com/jquery/how-do-i-use-jquery-select--to-select-multiple-options)