# How do I create a modal using ReactJS?
// plain

Creating a modal using ReactJS is fairly simple. First, you'll need to create a React component for the modal. This component should render the modal's HTML, which should include a container, a header, and a body.

```
import React, { Component } from 'react';

class Modal extends Component {
  render() {
    return (
      <div className="modal">
        <div className="modal-header">
          Modal Header
        </div>
        <div className="modal-body">
          Modal Body
        </div>
      </div>
    );
  }
}

export default Modal;
```

Then, you'll need to create a state variable to control whether the modal is visible or not. This can be done in the component's constructor.

```
import React, { Component } from 'react';

class Modal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isVisible: false,
    };
  }

  render() {
    return (
      <div className="modal">
        <div className="modal-header">
          Modal Header
        </div>
        <div className="modal-body">
          Modal Body
        </div>
      </div>
    );
  }
}

export default Modal;
```

Finally, you'll need to create a method to toggle the modal's visibility. This can be done by creating a method that sets the state variable to the opposite of its current state.

```
import React, { Component } from 'react';

class Modal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isVisible: false,
    };
  }

  toggleModal = () => {
    this.setState({
      isVisible: !this.state.isVisible,
    });
  }

  render() {
    return (
      <div className="modal">
        <div className="modal-header">
          Modal Header
        </div>
        <div className="modal-body">
          Modal Body
        </div>
      </div>
    );
  }
}

export default Modal;
```

You can then use this method to toggle the modal's visibility.

## Code explanation


1. Create a React component for the modal: This component should render the modal's HTML, which should include a container, a header, and a body.
2. Create a state variable to control whether the modal is visible or not: This can be done in the component's constructor.
3. Create a method to toggle the modal's visibility: This can be done by creating a method that sets the state variable to the opposite of its current state.

## Helpful links

- [React Modal Tutorial](https://blog.logrocket.com/react-modal-tutorial/)
- [React Modal Component](https://reactjs.org/docs/modal-component.html)

onelinerhub: [How do I create a modal using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-a-modal-using-reactjs)