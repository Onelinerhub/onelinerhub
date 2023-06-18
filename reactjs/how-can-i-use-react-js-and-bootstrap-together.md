# How can I use React.js and Bootstrap together?
// plain

React.js and Bootstrap can be used together to create user interfaces with a modern look and feel.

To use them together, we need to install the Bootstrap package for React. We can do this with npm:

```
npm install react-bootstrap bootstrap
```

Once the packages are installed, we can import Bootstrap components into our React components. For example, to create a simple alert box:

```
import { Alert } from 'react-bootstrap';

// ...

<Alert variant="success">
  <Alert.Heading>Well done!</Alert.Heading>
  <p>
    Aww yeah, you successfully read this important alert message. This example
    text is going to run a bit longer so that you can see how spacing within an
    alert works with this kind of content.
  </p>
</Alert>
```

This code will render a Bootstrap alert box inside the React component:

```
<div role="alert" class="alert alert-success">
  <h4 class="alert-heading">Well done!</h4>
  <p>
    Aww yeah, you successfully read this important alert message. This example
    text is going to run a bit longer so that you can see how spacing within an
    alert works with this kind of content.
  </p>
</div>
```

We can use any of the Bootstrap components in our React application in the same way.

## Helpful links
- https://react-bootstrap.github.io/
- https://getbootstrap.com/

onelinerhub: [How can I use React.js and Bootstrap together?](https://onelinerhub.com/reactjs/how-can-i-use-react-js-and-bootstrap-together)