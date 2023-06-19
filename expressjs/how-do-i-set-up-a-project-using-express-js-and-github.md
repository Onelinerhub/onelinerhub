# How do I set up a project using Express.js and GitHub?
// plain

1. Create a repository on GitHub:
   - Go to [GitHub](https://github.com) and log in with your credentials.
   - Click on the plus icon in the top right corner and select **New repository**.
   - Enter the repository name and click **Create repository**.

2. Clone the repository to your local machine:
   - Copy the repository URL from the GitHub page.
   - Open the terminal and navigate to the folder where you want to clone the repository.
   - Enter `git clone <repository-url>` and press enter.

3. Initialize a new Node.js project:
   - Navigate to the repository folder.
   - Enter `npm init` and press enter.
   - Follow the instructions to create a `package.json` file.

4. Install Express.js:
   - Enter `npm install express --save` and press enter.
   - This will install Express.js and add it to the `package.json` file.

5. Create an `app.js` file and add the following code:
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server is listening on port 3000');
});
```
   - This will create an Express.js server that listens on port 3000 and responds with `Hello World!` when the root URL is accessed.

6. Start the server:
   - Enter `node app.js` and press enter.
   - This will start the Express.js server.

7. Access the server:
   - Open your browser and go to `http://localhost:3000`
   - You should see the `Hello World!` message.

## Helpful links
- [GitHub](https://github.com)
- [Node.js](https://nodejs.org)
- [Express.js](https://expressjs.com)

onelinerhub: [How do I set up a project using Express.js and GitHub?](https://onelinerhub.com/expressjs/how-do-i-set-up-a-project-using-express-js-and-github)