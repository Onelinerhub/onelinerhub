# How to get IP address

```js
const os = require('os');
const net = os.networkInterfaces();

let ip = net.eth0[0].address;
```

- `require('os')` - module to work with `OS`
- `.networkInterfaces()` - returns data on all network interfaces
- `net.eth0[0].address` - returns first IP address of `eth0` interface

group: hostname

## Example: 
```js
const os = require('os');
const net = os.networkInterfaces();

console.log(net.eth0[0].address);
```
```
135.181.98.214

```

