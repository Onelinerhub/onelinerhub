# Use variable as regex

```javascript
var regex = new RegExp('[0-9]+', 'g');
var matches = 'test_str_1'.match(regex);
```

- var regex - declares new regular expression from string
- '[0-9]+' - string representation of our regular expression
- 'g' - which modifiers to use (global in this case)
- matches - will contain an array of found matches
- 'test_str_1'.match(regex) - matches text string ```'test_str_1'``` agains our ```regex``` regular expression
