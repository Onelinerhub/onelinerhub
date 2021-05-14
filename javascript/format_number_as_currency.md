# Format number as currency string (money)

```javascript
(new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' })).format(99999);
```

- new Intl.NumberFormat - instantiates JS native formatter ([docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat))
- style: 'currency', currency: 'USD' - pick currency style and set the currency itself
- 99999 - number we're going to format as money
