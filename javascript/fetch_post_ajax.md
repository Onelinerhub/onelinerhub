# Ajax post json data 

```javascript
fetch('/backend.php', {
  method: 'post',
  body: JSON.stringify({name: 'Donald'})
}).then(function(r) {
  return r.json();
}).then(function(data) {
  console.log(data);
});
```

- /backend.php - backend script to receive posted data
- method: 'post' - set ajax request method to post
- {name: 'Donald'} - this will be posted as JSON
- return r.json() - server response will be processed as JSON
- console.log(data) - replace with your code processing ```data``` (response from server as JSON object)

group: ajax_post
