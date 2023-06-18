# How do I use ReactJS to get the user's location?
// plain

In order to get the user's location using ReactJS, you need to use the `navigator.geolocation` API. The `navigator.geolocation` API provides access to the device's location data.

Below is an example of how to use the `navigator.geolocation` API within a React component:

```javascript
class MyComponent extends React.Component {
  componentDidMount() {
    navigator.geolocation.getCurrentPosition(
      position => {
        console.log(position.coords.latitude, position.coords.longitude);
      },
      err => console.log(err)
    );
  }
  render() {
    return <div>My Component</div>;
  }
}
```
This will output the user's latitude and longitude to the console.

The code above consists of the following parts:

1. `class MyComponent extends React.Component`: This declares a class component named `MyComponent`.
2. `componentDidMount()`: This is a React lifecycle method that is called when the component is mounted.
3. `navigator.geolocation.getCurrentPosition()`: This is the function that is used to get the user's location. It takes two arguments, a success callback and an error callback.
4. `position => { ... }`: This is the success callback that is called when the location is successfully retrieved. It takes the position object as an argument.
5. `err => console.log(err)`: This is the error callback that is called when there is an error retrieving the user's location. It takes the error object as an argument.
6. `console.log(position.coords.latitude, position.coords.longitude)`: This logs the user's latitude and longitude to the console.

## Helpful links

- [MDN - Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)
- [React - React Component API](https://reactjs.org/docs/react-component.html)

onelinerhub: [How do I use ReactJS to get the user's location?](https://onelinerhub.com/reactjs/how-do-i-use-reactjs-to-get-the-user-s-location)