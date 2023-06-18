# How do I quickly get started with ReactJS?
// plain

Getting started with ReactJS is relatively easy and can be done quickly.

1. Install the React library:

```
npm install react
```

2. Create a React component, for example:

```
import React from 'react';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello World</h1>
      </div>
    );
  }
}

export default App;
```

3. Render the component to the DOM:

```
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

4. Include the script tags in your HTML page:

```
<script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
```

This will render the component to the DOM with the output:

```
<div>
  <h1>Hello World</h1>
</div>
```

You can find more detailed instructions and helpful resources at the [ReactJS Documentation](https://reactjs.org/docs/getting-started.html).

onelinerhub: [How do I quickly get started with ReactJS?](https://onelinerhub.com/reactjs/how-do-i-quickly-get-started-with-reactjs)