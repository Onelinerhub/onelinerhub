# How can I use an AngularJS pipe to format a date?
// plain

An AngularJS pipe can be used to format a date by using the `date` pipe. This pipe takes in a date as an argument and formats it according to the parameters you provide.

For example, the following code:

```
<p>{{date | date:'MM/dd/yyyy'}}</p>
```

would output the current date in the format `MM/dd/yyyy`:

```
12/01/2020
```

The `date` pipe has several parameters that can be used to customize the output format:

- `MM`: The month as a number with leading zero (01-12).
- `dd`: The day as a number with leading zero (01-31).
- `yyyy`: The four-digit year.
- `EEE`: The abbreviated day of the week (Mon-Sun).
- `hh`: The hour as a number with leading zero (00-23).
- `mm`: The minute as a number with leading zero (00-59).
- `ss`: The second as a number with leading zero (00-59).

For more information about the `date` pipe, please refer to the [Angular documentation](https://angular.io/api/common/DatePipe).

onelinerhub: [How can I use an AngularJS pipe to format a date?](https://onelinerhub.com/angularjs/how-can-i-use-an-angularjs-pipe-to-format-a-date)