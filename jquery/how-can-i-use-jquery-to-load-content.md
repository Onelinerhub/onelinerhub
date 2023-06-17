# How can I use jQuery to load content?
// plain

jQuery makes it easy to load content into a webpage without refreshing the page. To do this, you can use the jQuery `load()` function.

Example code block:
```
$('#result').load('ajax/test.html');
```

This code will load the content of the file `test.html` into the element with the ID `result`.

## Code explanation

- `$('#result')`: This part of the code selects the element with the ID `result`.
- `load`: This is the jQuery `load()` function.
- `'ajax/test.html'`: This is the URL of the file that is being loaded.

## Helpful links
- [jQuery .load() function](http://api.jquery.com/load/)
- [jQuery Selectors](http://api.jquery.com/category/selectors/)

onelinerhub: [How can I use jQuery to load content?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-load-content)