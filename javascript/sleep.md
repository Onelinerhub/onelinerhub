# Sleep

```javascript
 const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
```

- new Promise - declares promise that executes standard timeout
- ms - number of milliseconds to stop execution for
- await - will pause code until promise is fullfilled (resolved)

## Example
```javascript
sleep(2 * 1000);
```
```bash
# will pause execution for 2 seconds
```
