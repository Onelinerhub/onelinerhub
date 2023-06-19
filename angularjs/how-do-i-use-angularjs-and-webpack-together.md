# How do I use AngularJS and Webpack together?
// plain

Using AngularJS and Webpack together is a great way to build and deploy your web applications. Webpack is a powerful tool that allows you to bundle and minify your JavaScript and CSS files, making them more efficient and easier to maintain.

To get started, you will need to install the webpack and angular-webpack-plugin packages.

```
npm install webpack angular-webpack-plugin --save
```

Once those packages are installed, you will need to create a webpack configuration file. This file will tell webpack how to bundle and minify your files.

```
const path = require('path');
const AngularWebpackPlugin = require('angular-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  plugins: [
    new AngularWebpackPlugin({
      root: 'app'
    })
  ]
};
```

The webpack configuration file tells webpack to take all of the files in the `src` directory and bundle them together into a single `bundle.js` file in the `dist` directory. The `AngularWebpackPlugin` tells webpack to look for an `app` directory, which is where your AngularJS application will be located.

Once you have your webpack configuration set up, you can then use webpack to bundle and minify your application.

```
webpack
```

The output of this command will be a single `bundle.js` file in your `dist` directory. This file can then be included in your HTML page, and your AngularJS application will be ready to use.

**## Helpful links**

- [Webpack Documentation](https://webpack.js.org/concepts/)
- [Angular-Webpack-Plugin Documentation](https://github.com/d3viant0ne/angular-webpack-plugin)

onelinerhub: [How do I use AngularJS and Webpack together?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-and-webpack-together)