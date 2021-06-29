# Sleep

```javascript
 const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
```

- new Promise - declares promise that executes standard timeout
- ms - number of milliseconds to stop execution for
- usage - ``` await sleep(2000); ```
- await - will pause code until promise is fullfilled (resolved)
