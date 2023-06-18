# How do ReactJS and React Native differ?
// plain

ReactJS and React Native are two different technologies that share the same codebase. ReactJS is a JavaScript library used for building user interfaces, while React Native is a mobile development framework used for building mobile applications.

The main difference between ReactJS and React Native is that ReactJS is used for web development, while React Native is used for mobile development. ReactJS uses HTML, CSS, and JavaScript to create web applications, while React Native uses JavaScript and React to create mobile applications.

ReactJS code example:
```
import React from 'react';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello World!</h1>
      </div>
    );
  }
}
```

React Native code example:
```
import React from 'react';
import { View, Text } from 'react-native';

class App extends React.Component {
  render() {
    return (
      <View>
        <Text>Hello World!</Text>
      </View>
    );
  }
}
```

In ReactJS, the `<div>` element is used to create a container for the content, while in React Native, the `<View>` element is used. The `<h1>` element is used to create a heading in ReactJS, while the `<Text>` element is used in React Native.

ReactJS and React Native also differ in terms of performance. ReactJS applications are generally faster than React Native applications, as they are rendered on the client-side. However, React Native applications can provide a better user experience, as they are rendered on the device itself.

## Helpful links
- [ReactJS](https://reactjs.org/)
- [React Native](https://reactnative.dev/)

onelinerhub: [How do ReactJS and React Native differ?](https://onelinerhub.com/reactjs/how-do-reactjs-and-react-native-differ)