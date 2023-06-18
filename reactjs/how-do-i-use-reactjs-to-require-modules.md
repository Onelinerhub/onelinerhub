# How do I use ReactJS to require modules?
// plain

ReactJS uses ES6 import statements to require modules. To use a module, you just need to import it with an import statement, like so:

```
import React from 'react';
```

This statement imports the React object from the 'react' module.

To use a module's exported functions, you can use the dot notation, like so:

```
import React from 'react';

React.render();
```

This code calls the render() function from the imported React object.

You can also import multiple modules at once, like so:

```
import React, {Component} from 'react';
```

This statement imports the React object and the Component object from the 'react' module.

You can also import individual functions from a module, like so:

```
import {render} from 'react';

render();
```

This statement imports the render() function from the 'react' module and calls it.

ReactJS also supports named imports, like so:

```
import {render as renderReact} from 'react';

renderReact();
```

This statement imports the render() function from the 'react' module and calls it as renderReact().

For more information on how to use ReactJS to require modules, please refer to the [ReactJS docs](https://reactjs.org/docs/getting-started.html#using-a-module-system).

onelinerhub: [How do I use ReactJS to require modules?](https://onelinerhub.com/reactjs/how-do-i-use-reactjs-to-require-modules)