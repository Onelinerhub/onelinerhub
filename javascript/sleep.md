# Sleep

```javascript
await new Promise(resolve => setTimeout(resolve, 2 * 1000));
```

- new Promise - declares promise that executes standard timeout
- await - will pause code until promise is fullfilled (resolved)
- 2 * 1000 - wait for ```2``` seconds
