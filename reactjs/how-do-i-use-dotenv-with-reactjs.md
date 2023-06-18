# How do I use dotenv with ReactJS?
// plain

Using dotenv with ReactJS is a great way to manage environment variables. Environment variables are key-value pairs that can be used to store sensitive information such as API keys, database credentials, or other configuration settings.

Here's an example of how to use dotenv with ReactJS:

1. Install the dotenv package.
```
npm install dotenv
```

2. Create a file called .env in the root of your ReactJS project.

3. Add environment variables to the .env file.
```
API_KEY=my_api_key
DB_USER=my_db_user
DB_PASSWORD=my_db_password
```

4. Require the dotenv package and configure it in the entry point of your ReactJS application.
```js
require('dotenv').config();
```

5. Access the environment variables from within your React application.
```js
const apiKey = process.env.API_KEY;
const dbUser = process.env.DB_USER;
const dbPassword = process.env.DB_PASSWORD;
```

This is a great way to keep your environment variables secure and organized.

More information about using dotenv with ReactJS can be found here:
- [Using dotenv with React](https://www.npmjs.com/package/dotenv#usage-with-react)
- [React Environment Variables](https://create-react-app.dev/docs/adding-custom-environment-variables/)

onelinerhub: [How do I use dotenv with ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-dotenv-with-reactjs)