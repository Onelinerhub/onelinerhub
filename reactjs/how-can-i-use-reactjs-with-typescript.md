# How can I use ReactJS with TypeScript?
// plain

ReactJS is a popular JavaScript library for building user interfaces, and TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. Together, they can be used to create powerful and dynamic web applications.

To use ReactJS with TypeScript, you must first install the React and TypeScript type definitions using the following command:

```
npm install --save-dev @types/react @types/react-dom
```

Then, you can create a TypeScript file with the extension `.tsx` to enable the TypeScript compiler to process React components. For example, the following code creates a simple React component in TypeScript:

```
import * as React from "react";

interface Props {
  name: string;
}

const Hello: React.FC<Props> = ({ name }) => {
  return <h1>Hello {name}!</h1>;
};

export default Hello;
```

The code above:
- Imports the React library (`import * as React from "react";`)
- Creates an interface for the component's props (`interface Props { name: string; }`)
- Creates a functional component with a generic type parameter (`const Hello: React.FC<Props> = ({ name }) => {`)
- Returns a React element (`return <h1>Hello {name}!</h1>;`)
- Exports the component (`export default Hello;`)

Finally, you can use the component in another TypeScript file with the following code:

```
import React from "react";
import ReactDOM from "react-dom";
import Hello from "./Hello";

ReactDOM.render(<Hello name="World" />, document.getElementById("root"));
```

The code above:
- Imports the React and ReactDOM libraries (`import React from "react"; import ReactDOM from "react-dom";`)
- Imports the component (`import Hello from "./Hello";`)
- Renders the component in the DOM (`ReactDOM.render(<Hello name="World" />, document.getElementById("root"));`)

## Helpful links
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/home.html)

onelinerhub: [How can I use ReactJS with TypeScript?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-with-typescript)