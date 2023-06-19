# How do I format a date in AngularJS?
// plain

AngularJS provides a great way to format dates using the `date` filter. This filter can be used in HTML templates as well as in JavaScript code.

The general syntax for the `date` filter is as follows:
```
{{ expression | date : format : timezone }}
```

- `expression` is the date object or a number (milliseconds since UTC epoch)
- `format` is a string of tokens that represent the output format
- `timezone` is an optional parameter that specifies the timezone to use

For example, to format a date object `myDate` to show the date in the format `dd/MM/yyyy`, we can use the following code:
```
{{ myDate | date : 'dd/MM/yyyy' }}
```

The output of the above code would be something like `10/07/2020`.

The `format` parameter accepts a wide range of tokens that can be used to customize the output. A full list of supported tokens can be found [here](https://docs.angularjs.org/api/ng/filter/date).

## Helpful links
- [AngularJS Date Filter](https://docs.angularjs.org/api/ng/filter/date)

onelinerhub: [How do I format a date in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-format-a-date-in-angularjs)