# How can I convert a Base64 string to a Blob object using ReactJS?
// plain

Using ReactJS, you can convert a Base64 string to a Blob object. This can be done by using the `btoa()` and `atob()` functions.

## Example code

```
const base64String = 'SGVsbG8gV29ybGQ=';
const blob = new Blob([atob(base64String)], { type: 'text/plain' });
```

The `btoa()` function encodes a string in base-64, while the `atob()` function decodes a base-64 encoded string. The `atob()` function is used to decode the Base64 string, and then the `Blob()` constructor is used to create a new Blob object. The `type` parameter is used to specify the type of data stored in the Blob.

## Code explanation

1. `const base64String = 'SGVsbG8gV29ybGQ=';` - This line creates a constant `base64String` that stores the Base64 string that needs to be converted.
2. `const blob = new Blob([atob(base64String)], { type: 'text/plain' });` - This line creates a new `Blob` object by using the `Blob()` constructor. The `atob()` function is used to decode the `base64String` and the `type` parameter is used to specify the type of data stored in the Blob.

## Helpful links
1. [MDN Docs - btoa()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/btoa)
2. [MDN Docs - atob()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/atob)
3. [MDN Docs - Blob()](https://developer.mozilla.org/en-US/docs/Web/API/Blob)

onelinerhub: [How can I convert a Base64 string to a Blob object using ReactJS?](https://onelinerhub.com/reactjs/how-can-i-convert-a-base---string-to-a-blob-object-using-reactjs)