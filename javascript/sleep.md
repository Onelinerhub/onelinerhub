# Sleep

```javascript
 const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
```

- new Promise - declares promise that executes standard timeout
- ms - number of milliseconds to stop execution for
- 
## Example
```javascript
// some code ...
await sleep(2 * 1000);
// some code after 2 seconds sleep
```
