# How do I add a link to my ReactJS application?
// plain

Adding a link to a ReactJS application is a relatively simple process. The following example code block shows how to create a link component with a URL:

```
import React from 'react';

const Link = ({url}) => (
  <a href={url}>Link</a>
);

export default Link;
```

This code creates a `Link` component that can be used to render a link to a given URL. To use this component, it must be imported into the component that needs to render the link. For example:

```
import React from 'react';
import Link from './Link';

const MyComponent = () => (
  <div>
    <Link url="https://www.example.com" />
  </div>
);

export default MyComponent;
```

This code will render a link to `https://www.example.com` on the page.

## Code explanation


- `import React from 'react';` imports the React library into the component.
- `const Link = ({url}) => (` creates a new React component called `Link` that takes a `url` property.
- `<a href={url}>Link</a>` renders an anchor element with the given `url` as its `href` attribute.
- `export default Link;` exports the `Link` component so it can be imported elsewhere.
- `import Link from './Link';` imports the `Link` component into the current component.
- `<Link url="https://www.example.com" />` renders the `Link` component with the given URL.

For more information on creating links in ReactJS, see the [React documentation](https://reactjs.org/docs/dom-elements.html#links).

onelinerhub: [How do I add a link to my ReactJS application?](https://onelinerhub.com/reactjs/how-do-i-add-a-link-to-my-reactjs-application)