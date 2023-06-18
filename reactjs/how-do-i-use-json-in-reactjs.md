# How do I use JSON in ReactJS?
// plain

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is used to exchange data between a server and a client. ReactJS is a popular JavaScript library for building user interfaces, and it has built-in support for working with JSON data.

In ReactJS, you can use the `fetch()` API to make an AJAX request and get the response in JSON format. Here is an example of how to use `fetch()` to get a JSON response from a server:

```js
fetch('http://example.com/data.json')
  .then(response => response.json())
  .then(data => console.log(data))
```

This will make an AJAX request to the URL `http://example.com/data.json` and log the response JSON data to the console.

Once you have the JSON data, you can use it in your React components. For example, you can use the `map()` function to loop over the data and render a list of items:

```js
const MyComponent = ({ data }) => {
  return (
    <ul>
      {data.map(item => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  )
}
```

This example will render a list of items from the `data` array, using the `id` and `name` properties of each item.

You can also use the `JSON.stringify()` function to convert a JavaScript object into a JSON string, which can be used to send data to a server. For example:

```js
const data = {
  name: 'John Doe',
  age: 42
}

fetch('http://example.com/save-data', {
  method: 'POST',
  body: JSON.stringify(data)
})
```

This example will make a POST request to the URL `http://example.com/save-data`, sending the `data` object as a JSON string.

## Helpful links
- [MDN - Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [React - Working with JSON](https://reactjs.org/docs/working-with-the-data.html#working-with-json)

onelinerhub: [How do I use JSON in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-json-in-reactjs)