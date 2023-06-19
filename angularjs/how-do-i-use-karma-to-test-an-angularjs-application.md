# How do I use Karma to test an AngularJS application?
// plain

Karma is a tool that can be used to test an AngularJS application. It is a test runner for JavaScript that runs on Node.js and is used to execute tests on real browsers and real devices.

To use Karma, you need to install it first. You can do this by running the following command in the terminal:

```
npm install -g karma
```

Once Karma is installed, you can create a configuration file which will tell Karma how to run the tests. This configuration file should be named `karma.conf.js` and should include the following code:

```
module.exports = function (config) {
  config.set({
    basePath: '',
    frameworks: ['jasmine', '@angular-devkit/build-angular'],
    plugins: [
      require('karma-jasmine'),
      require('karma-chrome-launcher'),
      require('karma-jasmine-html-reporter'),
      require('karma-coverage-istanbul-reporter'),
      require('@angular-devkit/build-angular/plugins/karma')
    ],
    client: {
      clearContext: false // leave Jasmine Spec Runner output visible in browser
    },
    coverageIstanbulReporter: {
      dir: require('path').join(__dirname, './coverage/my-app'),
      reports: ['html', 'lcovonly', 'text-summary'],
      fixWebpackSourcePaths: true
    },
    reporters: ['progress', 'kjhtml'],
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['Chrome'],
    singleRun: false,
    restartOnFileChange: true
  });
};
```

The code above sets up the configuration for Karma. It tells Karma which frameworks and plugins to use, and which browsers to run the tests on. After this configuration is set up, you can run your tests with the following command:

```
karma start karma.conf.js
```

This will execute the tests and output the results.

Parts of the code:
- `module.exports = function (config)`: This is the function that is exported from the configuration file. It sets up the configuration for Karma.
- `frameworks: ['jasmine', '@angular-devkit/build-angular']`: This tells Karma which frameworks to use. In this case, it is using Jasmine and the Angular Devkit.
- `plugins: [...]`: This is an array of plugins that Karma will use. These plugins are used to run tests, generate reports, and more.
- `browsers: ['Chrome']`: This tells Karma which browsers to run the tests on. In this case, it is running the tests on Chrome.

## Helpful links
- [Karma Documentation](https://karma-runner.github.io/latest/index.html)
- [Angular Devkit Documentation](https://angular.io/guide/angular-devkit)

onelinerhub: [How do I use Karma to test an AngularJS application?](https://onelinerhub.com/angularjs/how-do-i-use-karma-to-test-an-angularjs-application)