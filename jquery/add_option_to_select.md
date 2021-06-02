# Add new option (menu item) to select box (dropdown)

```javascript
$('select').append($('<option>', { value: 15, text: 'Title' }));
```

- 'select' - selector for the needed select box
- append( - will append specified element to our select box
- $('\<option\>' - creates new ```option``` element with specified attributes
- value: 15, text: 'Title' - new option final html: ```<option value="15">Title</option>```
