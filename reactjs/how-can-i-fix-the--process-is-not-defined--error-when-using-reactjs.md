# How can I fix the "process is not defined" error when using ReactJS?
// plain

The "process is not defined" error is a common issue when using ReactJS. This error occurs when the process global variable is not defined. The process global variable is defined in Node.js and is not available in the browser.

To fix this error, you need to use a library like `process.env` or `dotenv` to access environment variables in the browser.

For example, using `dotenv`:

```javascript
// In your .env file
REACT_APP_API_KEY=123

// In your application code
import dotenv from 'dotenv';

dotenv.config();

console.log(process.env.REACT_APP_API_KEY); // Output: 123
```

The code above imports the `dotenv` library, loads the `.env` file and logs the value of the `REACT_APP_API_KEY` environment variable.

To learn more about how to use `dotenv` to access environment variables in ReactJS, please refer to the following links:

- [The Basics Of Environment Variables In React](https://daveceddia.com/environment-variables-in-react/)
- [Using dotenv with Create React App](https://create-react-app.dev/docs/adding-custom-environment-variables/)

onelinerhub: [How can I fix the "process is not defined" error when using ReactJS?](https://onelinerhub.com/reactjs/how-can-i-fix-the--process-is-not-defined--error-when-using-reactjs)