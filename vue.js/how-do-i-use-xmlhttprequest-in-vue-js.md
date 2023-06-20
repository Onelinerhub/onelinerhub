# How do I use XMLHttpRequest in Vue.js?
// plain

Using XMLHttpRequest in Vue.js is quite simple. First, you need to import the `XMLHttpRequest` object from the `xmlhttprequest` library:
```js
import { XMLHttpRequest } from 'xmlhttprequest';
```
Then, you can create an `XMLHttpRequest` instance and use it to perform an HTTP request:
```js
const xhr = new XMLHttpRequest();
xhr.open('GET', 'http://example.com/api/data');
xhr.send();
```
The `send` method will send the request to the server and the response will be available in the `responseText` property of the `XMLHttpRequest` instance.

You can also add event listeners to the `XMLHttpRequest` instance to handle the response when it arrives:
```js
xhr.addEventListener('load', () => {
  console.log(xhr.responseText);
});
```

In summary, the steps to use XMLHttpRequest in Vue.js are:

1. Import the `XMLHttpRequest` object from the `xmlhttprequest` library.
2. Create an `XMLHttpRequest` instance.
3. Use the `open` and `send` methods to make the HTTP request.
4. Handle the response using the `responseText` property or an event listener.

## Helpful links
- [XMLHttpRequest Documentation](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
- [Vue.js Documentation](https://vuejs.org/v2/guide/)

onelinerhub: [How do I use XMLHttpRequest in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-xmlhttprequest-in-vue-js)