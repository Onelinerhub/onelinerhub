# How do I set up a YAML configuration file for a Node.js Express application?
// plain

Setting up a YAML configuration file for a Node.js Express application is relatively straightforward. The following code block provides an example of how to do this:

```
server:
  port: 3000
database:
  url: mongodb://localhost:27017/myapp
```

This example YAML configuration file contains two sections: one for the server and one for the database. The server section contains the port number, while the database section contains the URL for the MongoDB database.

The configuration file can then be read in the Express application using the [js-yaml](https://github.com/nodeca/js-yaml) library.

```
const yaml = require('js-yaml');
const fs = require('fs');

let config;
try {
  config = yaml.safeLoad(fs.readFileSync('./config.yml', 'utf8'));
  console.log(config);
} catch (e) {
  console.log(e);
}
```

This code block reads the configuration file and stores the configuration in a `config` object. The output of this code would look like this:

```
{ server: { port: 3000 },
  database: { url: 'mongodb://localhost:27017/myapp' } }
```

For further information, please refer to the [js-yaml documentation](https://github.com/nodeca/js-yaml).

onelinerhub: [How do I set up a YAML configuration file for a Node.js Express application?](https://onelinerhub.com/expressjs/how-do-i-set-up-a-yaml-configuration-file-for-a-node-js-express-application)