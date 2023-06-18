# How can I use React.js and AJAX to make API calls?
// plain

React.js and AJAX can be used together to make API calls. Here's an example of how to do this:

```
import React from 'react';
import axios from 'axios';

class App extends React.Component {
  state = {
    data: null
  }

  componentDidMount() {
    const url = 'https://example.com/api';
    axios.get(url)
      .then(response => {
        this.setState({ data: response.data });
      })
      .catch(error => {
        console.log(error);
      });
  }

  render() {
    return (
      <div>
        {this.state.data && <p>{this.state.data.message}</p>}
      </div>
    );
  }
}

export default App;
```

The code above:
- Imports React and axios at the top of the file
- Defines the `App` class which extends `React.Component`
- Defines the `state` of the component, which is set to an empty object
- Uses the `componentDidMount` lifecycle method to make an AJAX call to the API
- Uses the `setState` method to update the `state` with the data from the API call
- Renders the data from the API call in the `render` method

## Helpful links
- [React Docs](https://reactjs.org/docs/getting-started.html)
- [Axios Docs](https://github.com/axios/axios)

onelinerhub: [How can I use React.js and AJAX to make API calls?](https://onelinerhub.com/reactjs/how-can-i-use-react-js-and-ajax-to-make-api-calls)