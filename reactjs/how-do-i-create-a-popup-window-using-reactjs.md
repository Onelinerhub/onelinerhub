# How do I create a popup window using ReactJS?
// plain

Creating a popup window using ReactJS is a simple process. To do this, you'll need to use the `ReactDOM.createPortal()` method. This method takes two arguments: the React element you want to render, and the DOM element you want to render it into.

For example, let's say you want to render a simple popup window with a message inside. The code would look like this:

```javascript
import React from 'react';
import { createPortal } from 'react-dom';

const Popup = ({ message }) =>
  createPortal(
    <div>
      <h1>{message}</h1>
    </div>,
    document.body
  );

ReactDOM.render(<Popup message="Hello World!" />, document.getElementById('root'));
```

This code will render a popup window with the message "Hello World!" inside.

Here's a breakdown of the code:

- `import React from 'react'`: This imports the React library.
- `import { createPortal } from 'react-dom'`: This imports the `createPortal` method from `react-dom`.
- `const Popup = ({ message }) =>`: This is a React component that takes a `message` prop and renders a popup window with the message inside.
- `createPortal(<div><h1>{message}</h1></div>, document.body)`: This uses the `createPortal` method to render the `<div>` element into the `document.body` element.
- `ReactDOM.render(<Popup message="Hello World!" />, document.getElementById('root'))`: This renders the `Popup` component into the element with the `id` of `root`.

For more information on creating popup windows with ReactJS, check out the [React documentation](https://reactjs.org/docs/portals.html).

onelinerhub: [How do I create a popup window using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-a-popup-window-using-reactjs)