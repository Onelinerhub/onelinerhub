# How do I create a link using jQuery?
// plain

Creating a link using jQuery is a simple process. To do this, first create a jQuery selector for the element you want to link to. Then, use the `attr()` method to set the `href` attribute of the element to the URL you want to link to. Here is an example of how to create a link using jQuery:

```
<div id="myLink">Link Text</div>

<script>
  $('#myLink').attr('href', 'http://www.example.com');
</script>
```

This code will create a link with the text "Link Text" that links to the URL `http://www.example.com`.

The code can be broken down into the following parts:

1. `$('#myLink')` - This is the jQuery selector for the element with the ID `myLink`.
2. `attr('href', 'http://www.example.com')` - This is the `attr()` method, which is used to set the `href` attribute of the element to the URL `http://www.example.com`.

## Helpful links

- [jQuery Attr() Method](https://api.jquery.com/attr/)

onelinerhub: [How do I create a link using jQuery?](https://onelinerhub.com/jquery/how-do-i-create-a-link-using-jquery)