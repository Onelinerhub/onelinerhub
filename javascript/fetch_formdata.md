# Ajax post form (FormData) data with fetch

```javascript
fetch('/backend.php', {
  method: 'post',
  body: FormData(document.querySelector('form'))
}).then(function(r) {
  return r.json();
}).then(function(data) {
  console.log(data);
});
```

- /backend.php - backend script to receive posted data
- method: 'post' - set ajax request method to post
- querySelector('form') - select form object that needs to be posted
- return r.json() - server response will be processed as JSON
- console.log(data) - replace with your code processing ```data``` (response from server as JSON object)

group: ajax_post
