# How do I use AngularJS pipes to transform data?
// plain

AngularJS pipes are a powerful way to transform data. Pipes are a simple way to transform data in an Angular template. They are a great way to format strings, numbers, dates, and other values.

For example, the following code block uses the built-in `date` pipe to transform a date string into a formatted date string:

```
<p>{{ '2020-09-20' | date:'fullDate' }}</p>

// Output: Sunday, September 20, 2020
```

The code above has the following parts:

* `{{ '2020-09-20' }}` - This is the data that is being transformed. It is a date string in the format `YYYY-MM-DD`.

* `| date:'fullDate'` - This is the pipe that is being used to transform the data. In this case, it is the built-in `date` pipe, which is used to format a date string.

* `'fullDate'` - This is an argument that is being passed to the `date` pipe. This argument specifies the format that the date string should be transformed into. In this case, it is the `fullDate` format, which is a long date format.

For more information on AngularJS pipes, see the [Angular documentation](https://angular.io/guide/pipes).

onelinerhub: [How do I use AngularJS pipes to transform data?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-pipes-to-transform-data)