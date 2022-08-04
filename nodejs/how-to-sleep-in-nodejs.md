# How to sleep in Nodejs

```js
async function init() {
  console.log(new Date());
  await sleep(1500);
  console.log(new Date());
}

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

init();
```

- `sleep(` - custom function to sleep for a given number of milliseconds
- `new Promise(` - creates new promise
- `setTimeout` - calls given callback in a given number of milliseconds
- `await sleep(1500);` - will synchronously sleep for 1.5 seconds

## Example: 
```js
async function init() {
  console.log(new Date());
  await sleep(1500);
  console.log(new Date());
}

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

init();
```
```
2022-08-04T11:08:11.484Z
2022-08-04T11:08:12.990Z

```

