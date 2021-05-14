# Format number as currency string (money)

```javascript
(new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' })).format(99999);
```

- new Intl.NumberFormat - instantiates JS formatter
- style: 'currency', currency: 'USD' - pick currency style and set the currency itself
- 99999 - number we're going to format as money
