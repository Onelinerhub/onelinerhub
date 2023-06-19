# How can I use Jest to test my Express.js application?
// plain

Jest is a popular JavaScript testing framework that can be used to test an Express.js application. To get started, install Jest and its Express-compatible adapter, SuperTest.

```
npm install --save-dev jest supertest
```

Once installed, create a test file for your Express application. The following example uses `app.test.js` as the name of the file:

```
// app.test.js
const request = require('supertest');
const app = require('./app');

describe('Test the root path', () => {
  test('It should response the GET method', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
  });
});
```

The code above imports the `request` method from the SuperTest package and the Express app from the `app.js` file. The `describe` and `test` methods are used to create a test suite and test case, respectively. The `request` method is used to make a request to the Express app, and the `expect` method is used to check the response status code.

To run the test, use the following command:

```
npm run test
```

The output should look something like this:

```
 PASS  app.test.js
  Test the root path
    ✓ It should response the GET method (3ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        2.9s
```

For more information on using Jest to test an Express application, see the [Jest documentation](https://jestjs.io/docs/en/tutorial-react-node) and the [SuperTest documentation](https://www.npmjs.com/package/supertest).

onelinerhub: [How can I use Jest to test my Express.js application?](https://onelinerhub.com/expressjs/how-can-i-use-jest-to-test-my-express-js-application)