# How can I use jQuery to reload a page?
// plain

You can use jQuery to reload a page by using the `location.reload()` method. This method will reload the page from the server.

## Example code

```
$(document).ready(function(){
  $('#reload-button').click(function(){
    location.reload();
  });
});
```
## Output example
 No output

## Code explanation

- `$(document).ready(function(){` - This part will wait until the DOM is ready before executing the code.
- `$('#reload-button').click(function(){` - This part will listen for a click event on the element with the id of `reload-button`.
- `location.reload();` - This part will reload the page from the server.

## Helpful links
- https://api.jquery.com/ready/
- https://api.jquery.com/click/
- https://developer.mozilla.org/en-US/docs/Web/API/Location/reload

onelinerhub: [How can I use jQuery to reload a page?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-reload-a-page)