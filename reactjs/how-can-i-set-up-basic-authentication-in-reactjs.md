# How can I set up basic authentication in ReactJS?
// plain

Setting up basic authentication in ReactJS is relatively easy. To do so, you must first install the `react-auth-wrapper` package:

```
npm install react-auth-wrapper
```

Once installed, you can wrap your components with the `withAuth` HOC, which provides the authentication logic and props to the wrapped component.

```
import { withAuth } from 'react-auth-wrapper';

const MyComponent = props => <div>My Component</div>

export default withAuth(MyComponent);
```

The `withAuth` HOC takes an options object as an optional second argument, which can be used to customize the authentication logic. This options object can include the following properties:

* `authenticator`: A function that takes the current props and returns a Promise that resolves with an authentication object or rejects with an error.
* `wrapperDisplayName`: A string that will be used as the display name for the wrapper component.
* `onAuthFail`: A function that will be called if authentication fails.

You can also add custom props to the wrapped component by providing a `mapProps` function to the options object. This function takes the current props and returns a new props object.

```
import { withAuth } from 'react-auth-wrapper';

const MyComponent = props => <div>My Component</div>

const mapProps = props => ({
  ...props,
  customProp: 'value'
});

export default withAuth(MyComponent, { mapProps });
```

For more information, please see the [`react-auth-wrapper` documentation](https://github.com/mjrussell/react-auth-wrapper).

onelinerhub: [How can I set up basic authentication in ReactJS?](https://onelinerhub.com/reactjs/how-can-i-set-up-basic-authentication-in-reactjs)