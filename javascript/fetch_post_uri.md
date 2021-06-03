# Ajax post x-www-form-urlencoded data 

```javascript
fetch('/backend.php', {
  method: 'post',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' },
  body: 'var1=' + encodeURIComponent('Donald Trump :(') + '&var2=123'
}).then(function(r) {
  return r.json();
}).then(function(data) {
  console.log(data);
});
```

- /backend.php - backend script to receive posted data
- method: 'post' - set ajax request method to post
- headers: { 'Content-Type' - sets ```x-www-form-urlencoded``` data encoding
- body: - pass encoded variables and values separated by ```&```
- var1 - name of first variable to post
- 'Donald Trump :(' - value of ```var1``` variable to post which needs to be encoded
- return r.json() - server response will be processed as JSON
- console.log(data) - replace with your code processing ```data``` (response from server as JSON object)

group: ajax_post
