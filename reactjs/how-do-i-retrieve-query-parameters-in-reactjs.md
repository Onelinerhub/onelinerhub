# How do I retrieve query parameters in ReactJS?
// plain

In ReactJS, query parameters can be retrieved by using the `URLSearchParams` API. It is a built-in browser API that provides utility methods to work with query strings.

## Example code

```
// Get the current URL
const url = window.location.href;

// Create an object with the URL's query parameters
const params = new URLSearchParams(url.split('?')[1]);

// Get the value of the `name` query parameter
const name = params.get('name');
```

## Output example

`name`

## Code explanation

- `window.location.href` - The current URL
- `URLSearchParams` - A built-in browser API that provides utility methods to work with query strings
- `url.split('?')[1]` - Splits the URL into two parts, the first part being the path and the second part being the query string
- `params.get('name')` - Retrieves the value of the `name` query parameter

## Helpful links
- [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) - MDN web docs for URLSearchParams

onelinerhub: [How do I retrieve query parameters in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-retrieve-query-parameters-in-reactjs)