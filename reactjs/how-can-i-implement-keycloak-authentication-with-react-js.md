# How can I implement Keycloak authentication with React.js?
// plain

1. Install the Keycloak JavaScript adapter by running `npm install keycloak-js` in the terminal.

2. Create a Keycloak instance in your React component's `constructor` method, passing it the `initOptions` object.

```javascript
import Keycloak from 'keycloak-js';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { keycloak: null };
    const initOptions = {
      url: 'http://localhost:8080/auth',
      realm: 'master',
      clientId: 'my-react-app'
    };
    const keycloak = Keycloak(initOptions);
    this.state = { keycloak };
  }
  ...
}
```

3. Initialize the Keycloak instance by calling `keycloak.init()` and passing it a `success` and `error` callback.

```javascript
keycloak.init({ onLoad: 'login-required' }).success(authenticated => {
  this.setState({ authenticated });
}).error(err => {
  console.error(err);
});
```

4. Wrap the component's `render` method with a call to `keycloak.updateToken`, which will ensure that the token is up to date.

```javascript
render() {
  if (this.state.keycloak) {
    if (this.state.authenticated) {
      this.state.keycloak.updateToken(5).success(refreshed => {
        if (refreshed) {
          console.log('Token refreshed');
        } else {
          console.log('Token not refreshed');
        }
      }).error(err => console.error(err));
      ...
    }
  }
}
```

5. Use the `keycloak.token` property to obtain the token and pass it with the request headers when making API calls.

```javascript
axios.get('/api/data', {
  headers: {
    Authorization: 'Bearer ' + this.state.keycloak.token
  }
})
```

6. Log out the user by calling `keycloak.logout()`.

```javascript
keycloak.logout()
```

7. Finally, use the `keycloak.login()` method to redirect the user to the Keycloak login page.

```javascript
keycloak.login()
```

## Helpful links

- [Keycloak JS Adapter Documentation](https://www.keycloak.org/docs/latest/securing_apps/index.html#_javascript_adapter)
- [Keycloak JS Adapter GitHub Repo](https://github.com/keycloak/keycloak-js-bower)

onelinerhub: [How can I implement Keycloak authentication with React.js?](https://onelinerhub.com/reactjs/how-can-i-implement-keycloak-authentication-with-react-js)