# How do I use jQuery autocomplete to create a search box?
// plain

Using jQuery autocomplete to create a search box is simple. First, you need to include the jQuery library and jQuery UI library in the HTML document. Then, you need to create an input element with an ID and set the data source for the autocomplete widget. Here is an example code block:

```
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>
<input type="text" id="searchBox">
<script>
$( "#searchBox" ).autocomplete({
  source: [ "apple", "banana", "orange" ]
});
</script>
```

This code will create an input element and enable autocomplete on it with the given data source.

The parts of this code are:

1. Include jQuery library: `<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>`
2. Include jQuery UI library: `<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>`
3. Create an input element with an ID: `<input type="text" id="searchBox">`
4. Set the data source for the autocomplete widget: `source: [ "apple", "banana", "orange" ]`
5. Initialize the autocomplete widget on the input element: `$( "#searchBox" ).autocomplete({`

For more information on jQuery autocomplete, see the [jQuery UI Autocomplete documentation](https://api.jqueryui.com/autocomplete/).

onelinerhub: [How do I use jQuery autocomplete to create a search box?](https://onelinerhub.com/jquery/how-do-i-use-jquery-autocomplete-to-create-a-search-box)