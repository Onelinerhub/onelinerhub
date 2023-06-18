# How do I use ReactJS to render Markdown?
// plain

ReactJS can be used to render Markdown with the help of a library such as [React Markdown](https://github.com/rexxars/react-markdown). This library provides a React component that can be used to render markdown.

## Example code

```jsx
import React from 'react';
import ReactMarkdown from 'react-markdown';

const MyComponent = () => (
  <ReactMarkdown
    source={`
# This is a header

And this is a paragraph
`}
  />
);
```

## Output example


# This is a header

And this is a paragraph

The example code renders a header and a paragraph. It does this by importing the ReactMarkdown library and using the `ReactMarkdown` component. The `source` prop is used to pass in the markdown content to be rendered.

React Markdown also supports additional features such as custom renderers, HTML tags, and syntax highlighting. For more information, please refer to the [docs](https://github.com/rexxars/react-markdown/blob/master/README.md).

onelinerhub: [How do I use ReactJS to render Markdown?](https://onelinerhub.com/reactjs/how-do-i-use-reactjs-to-render-markdown)