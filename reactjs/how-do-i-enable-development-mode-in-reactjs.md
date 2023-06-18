# How do I enable development mode in ReactJS?
// plain

To enable development mode in ReactJS, you need to set the `NODE_ENV` environment variable to `development`.

## Example code

```
process.env.NODE_ENV = 'development';
```

This will enable React's development-only features, such as warning messages, and give you access to additional development tools.

## Code explanation

- `process`: This is the global Node.js object that contains information about the current process.
- `env`: This is an object that contains environment variables.
- `NODE_ENV`: This is the environment variable that is used to indicate the current environment.
- `development`: This is the value that should be assigned to the `NODE_ENV` environment variable to indicate that the application is running in development mode.

## Helpful links
- [Node.js Environment Variables](https://nodejs.org/api/process.html#process_process_env)
- [ReactJS Environment Variables](https://create-react-app.dev/docs/adding-custom-environment-variables/)

onelinerhub: [How do I enable development mode in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-enable-development-mode-in-reactjs)