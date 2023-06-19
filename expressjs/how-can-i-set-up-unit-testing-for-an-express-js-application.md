# How can I set up unit testing for an Express.js application?
// plain

Unit testing an Express.js application can be done using the popular testing framework [Mocha](https://mochajs.org/). Mocha provides a simple way to set up tests for your application.

To get started, install Mocha using npm:

```
npm install --save-dev mocha
```

Then create a `test` directory in your application root, and create a test file (e.g. `test/app.test.js`) with the following content:

```js
const assert = require('assert');
const request = require('supertest');
const app = require('../app');

describe('GET /', () => {
  it('should return 200 OK', (done) => {
    request(app)
      .get('/')
      .expect(200, done);
  });
});
```

This test will ensure that a `GET` request to the root `/` route returns a 200 status code.

Finally, add a script to your `package.json` file to run the tests:

```json
"scripts": {
  "test": "mocha"
}
```

Now you can run the tests from the command line with `npm test`:

```
npm test
```

This will print out the results of the tests.

## Helpful links
- [Mocha](https://mochajs.org/)
- [SuperTest](https://github.com/visionmedia/supertest)

onelinerhub: [How can I set up unit testing for an Express.js application?](https://onelinerhub.com/expressjs/how-can-i-set-up-unit-testing-for-an-express-js-application)