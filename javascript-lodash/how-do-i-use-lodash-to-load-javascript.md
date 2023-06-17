# How do I use lodash to load JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to load JavaScript files in a few different ways.

1. Using the `require()` function:
```
// Load lodash
const _ = require('lodash');

// Load a JavaScript file
_.require('./my-script.js');
```

2. Using the `import()` function:
```
// Load lodash
import _ from 'lodash';

// Load a JavaScript file
_.import('./my-script.js');
```

3. Using the `load()` function:
```
// Load lodash
const _ = require('lodash');

// Load a JavaScript file
_.load('./my-script.js');
```

These functions can be used to load any JavaScript file, including libraries, modules, and custom scripts.

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)
- [Node.js require() Documentation](https://nodejs.org/api/modules.html#modules_require)
- [ES6 import() Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)

onelinerhub: [How do I use lodash to load JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-load-javascript)