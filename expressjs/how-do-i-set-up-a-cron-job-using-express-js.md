# How do I set up a cron job using Express.js?
// plain

Setting up a cron job using Express.js is a simple process. The following example code will demonstrate how to set up a cron job that runs every minute:

```javascript
const cron = require('node-cron');

cron.schedule('* * * * *', () => {
  // Do something every minute
});
```

The code above contains the following parts:

* `const cron = require('node-cron');` - This line imports the `node-cron` module.

* `cron.schedule('* * * * *', () => {` - This line sets up a cron job that runs every minute. The first parameter is a string that contains the time pattern for the job. The `*` character indicates that the job should run every minute.

* `// Do something every minute` - This line is the code that will be run every minute.

* `});` - This line closes the callback function that will be run every minute.

For more information about setting up cron jobs with Express.js, please refer to the following links:

* [Node-cron documentation](https://www.npmjs.com/package/node-cron)
* [Express.js cron job example](https://www.npmjs.com/package/node-cron)

onelinerhub: [How do I set up a cron job using Express.js?](https://onelinerhub.com/expressjs/how-do-i-set-up-a-cron-job-using-express-js)