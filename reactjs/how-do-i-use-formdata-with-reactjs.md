# How do I use FormData with ReactJS?
// plain

FormData is a global JavaScript object that can be used to construct a set of key/value pairs which can be sent using XMLHttpRequest. It is used to send form data to a server in an asynchronous way.

In ReactJS, FormData can be used to send form data to a server. The following example shows how to create a FormData object and submit it using the fetch API:

```js
const formData = new FormData();
formData.append('name', 'John Doe');
formData.append('age', '20');

fetch('/api/submitFormData', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

The code above creates a FormData object and adds two key/value pairs to it. It then sends the FormData object to the server in an asynchronous way using the fetch API.

Here is a list of the parts of the code above and their explanations:

1. `const formData = new FormData();` - This creates a new FormData object.
2. `formData.append('name', 'John Doe');` - This adds a key/value pair to the FormData object.
3. `fetch('/api/submitFormData', {` - This sends the FormData object to the server using the fetch API.
4. `method: 'POST'` - This specifies that the request should be sent using the POST method.
5. `body: formData` - This specifies that the FormData object should be sent as the request body.

For more information, see [MDN's documentation on FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) and [React's documentation on Fetch API](https://reactjs.org/docs/faq-ajax.html#what-is-the-fetch-api).

onelinerhub: [How do I use FormData with ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-formdata-with-reactjs)