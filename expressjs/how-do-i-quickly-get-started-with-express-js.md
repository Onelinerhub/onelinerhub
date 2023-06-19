# How do I quickly get started with Express.js?
// plain

Getting started with Express.js is relatively simple. To quickly create an Express.js application, you can use the `express-generator` command line tool.

To install `express-generator`, open your terminal and run the following command:

```
npm install -g express-generator
```

Once you have `express-generator` installed, you can create an Express.js application by running the following command in your terminal:

```
express myapp
```

This will create a directory called `myapp` with the following structure:

```
myapp
├── app.js
├── bin
│   └── www
├── package.json
├── public
│   ├── images
│   ├── javascripts
│   └── stylesheets
│       └── style.css
├── routes
│   ├── index.js
│   └── users.js
└── views
    ├── error.jade
    ├── index.jade
    └── layout.jade
```

To start the application, `cd` into the `myapp` directory and run the following command:

```
npm start
```

This will start the Express.js application on port 3000. You can then access the application by going to `http://localhost:3000` in your browser.

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [Getting Started with Express.js](https://expressjs.com/en/starter/installing.html)

onelinerhub: [How do I quickly get started with Express.js?](https://onelinerhub.com/expressjs/how-do-i-quickly-get-started-with-express-js)