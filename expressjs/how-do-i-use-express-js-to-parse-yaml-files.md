# How do I use Express.js to parse YAML files?
// plain

Express.js is a web application framework for Node.js that is used for building web applications. It can be used to parse YAML files using the `js-yaml` module.

```
const express = require('express');
const yaml = require('js-yaml');

const app = express();

app.get('/', (req, res) => {
  const yamlString = `
  a: 1
  b: 2
  `;
  const data = yaml.load(yamlString);
  res.send(data);
});

app.listen(3000);
```
## Output example

```
{ a: 1, b: 2 }
```

The code above uses the following parts:

1. `const express = require('express');` - This imports the Express.js module.
2. `const yaml = require('js-yaml');` - This imports the `js-yaml` module, which is used to parse YAML files.
3. `const app = express();` - This creates an Express.js application.
4. `app.get('/', (req, res) => {` - This is a route handler for the root path `'/'` that is triggered when a GET request is sent to the server.
5. `const yamlString = ` - This is a string containing a YAML document.
6. `yaml.load(yamlString)` - This parses the YAML string and returns an object.
7. `res.send(data);` - This sends the parsed data as a response.
8. `app.listen(3000);` - This starts the server on port 3000.

## Helpful links

- [Express.js](https://expressjs.com/)
- [js-yaml](https://github.com/nodeca/js-yaml)

onelinerhub: [How do I use Express.js to parse YAML files?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-parse-yaml-files)