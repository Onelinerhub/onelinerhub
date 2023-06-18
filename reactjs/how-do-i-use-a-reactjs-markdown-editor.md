# How do I use a ReactJS Markdown editor?
// plain

To use a ReactJS Markdown editor you will need to install the [React Markdown Editor](https://github.com/rexxars/react-markdown-editor) package.

Once installed, you can use the following code to render the editor:

```js
import React from 'react';
import ReactMarkdownEditor from 'react-markdown-editor';

class MyEditor extends React.Component {
  render() {
    return (
      <div>
        <ReactMarkdownEditor />
      </div>
    );
  }
}
```

The editor will appear as a text area with a toolbar above it. The toolbar contains buttons for formatting text, creating links, and inserting images.

The editor also supports live preview of the Markdown text. To enable this feature, pass a `preview` prop to the `ReactMarkdownEditor` component:

```js
<ReactMarkdownEditor preview />
```

You can also customize the editor's appearance by passing a `styles` prop to the `ReactMarkdownEditor` component:

```js
const styles = {
  editor: {
    fontFamily: '"Fira code", "Fira Mono", monospace',
    fontSize: 16
  }
};

<ReactMarkdownEditor styles={styles} />
```

## Helpful links
* [React Markdown Editor](https://github.com/rexxars/react-markdown-editor)
* [Live preview](https://github.com/rexxars/react-markdown-editor#live-preview)
* [Custom styles](https://github.com/rexxars/react-markdown-editor#custom-styles)

onelinerhub: [How do I use a ReactJS Markdown editor?](https://onelinerhub.com/reactjs/how-do-i-use-a-reactjs-markdown-editor)