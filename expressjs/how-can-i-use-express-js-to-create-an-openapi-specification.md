# How can I use Express.js to create an OpenAPI specification?
// plain

Express.js is a web application framework for Node.js and can be used to create an OpenAPI specification. An OpenAPI specification is a machine-readable document that describes an API, such as its endpoints, operations, and parameters.

To create an OpenAPI specification with Express.js, the following steps should be taken:

1. Install the `swagger-ui-express` package:
    ```
    npm install swagger-ui-express
    ```

2. Create a new Express.js app:
    ```js
    const express = require('express');
    const app = express();
    ```

3. Add the `swagger-ui-express` middleware to the app:
    ```js
    const swaggerUi = require('swagger-ui-express');
    const swaggerDocument = require('./swagger.json');
    app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
    ```

4. Create a `swagger.json` file in the root of your project, which contains the OpenAPI specification:
    ```json
    {
      "openapi": "3.0.0",
      "info": {
        "title": "My API",
        "description": "API for my web app",
        "version": "1.0.0"
      },
      "paths": {
        "/users": {
          "get": {
            "summary": "Get all users",
            "responses": {
              "200": {
                "description": "A list of users"
              }
            }
          }
        }
      }
    }
    ```

5. Start the server:
    ```js
    const port = 3000;
    app.listen(port, () => {
      console.log(`Server started on port ${port}`);
    });
    ```
    Output: `Server started on port 3000`

6. Visit `http://localhost:3000/api-docs` in your browser to view the OpenAPI specification.

## Helpful links
- [Express.js](https://expressjs.com/)
- [Swagger UI Express](https://www.npmjs.com/package/swagger-ui-express)
- [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification)

onelinerhub: [How can I use Express.js to create an OpenAPI specification?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-create-an-openapi-specification)