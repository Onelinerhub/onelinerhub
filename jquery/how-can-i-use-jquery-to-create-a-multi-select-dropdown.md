# How can I use jQuery to create a multi-select dropdown?
// plain

jQuery can be used to create a multi-select dropdown. A multi-select dropdown is a dropdown menu with multiple selectable options. The following example code uses jQuery to create a multi-select dropdown:

```
<select multiple="multiple">
  <option value="1">Option 1</option>
  <option value="2">Option 2</option>
  <option value="3">Option 3</option>
  <option value="4">Option 4</option>
</select>

<script>
$("select").multiselect();
</script>
```

The code above will create a multi-select dropdown with four options. The user can select multiple options by holding down the `Ctrl` key while clicking on the options.

The code consists of two parts:

1. HTML code to create the dropdown menu with options:
   - `<select multiple="multiple">`: This creates the dropdown menu and sets the `multiple` attribute to `multiple` to enable multiple selection.
   - `<option>`: This creates each of the options in the dropdown menu.
2. jQuery code to enable multiple selection:
   - `$("select").multiselect()`: This uses jQuery to enable multiple selection on the dropdown menu.

For more information on creating multi-select dropdowns with jQuery, see the following links:

- [jQuery MultiSelect](https://github.com/nobleclem/jQuery-MultiSelect)
- [How to Create a Multi-Select Dropdown](https://www.formget.com/jquery-multi-select/)

onelinerhub: [How can I use jQuery to create a multi-select dropdown?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-create-a-multi-select-dropdown)