# How can I use ReactJS and LocalStorage together?
// plain

ReactJS and LocalStorage can be used together to store data on the client-side. LocalStorage is a key-value pair storage system that is available on modern web browsers. It can be used to store data that is required by the application for a period of time.

For example, we can use LocalStorage to store the user's authentication token when they log in. This token can then be used to authenticate the user when they make requests to the server.

To use ReactJS and LocalStorage together, we can use the `useState` hook to store the data in the component state. We can then use the `useEffect` hook to store the data in the LocalStorage when the component state changes.

## Example code

```
const [token, setToken] = useState(null);

useEffect(() => {
  localStorage.setItem('token', token);
}, [token]);
```

This code will store the token in the LocalStorage whenever the token in the component state changes.

The code can be broken down into the following parts:

1. `const [token, setToken] = useState(null);` - This line uses the `useState` hook to initialize the token in the component state.

2. `useEffect(() => {` - This line uses the `useEffect` hook to run a function whenever the token in the component state changes.

3. `localStorage.setItem('token', token);` - This line sets the token in the LocalStorage.

4. `}, [token]);` - This line closes the `useEffect` hook and specifies that the function should only run when the token in the component state changes.

## Helpful links

- [React useState Hook](https://reactjs.org/docs/hooks-state.html)
- [React useEffect Hook](https://reactjs.org/docs/hooks-effect.html)
- [LocalStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

onelinerhub: [How can I use ReactJS and LocalStorage together?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-and-localstorage-together)