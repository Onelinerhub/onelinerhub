# How can I use an AngularJS filter to format a date?
// plain

Using an AngularJS filter to format a date is a simple process. The following example code block uses the `date` filter to format a date into the `medium` date format:

```
{{ date_variable | date:'medium' }}
```

The output of this code block would be a date formatted as `Jan 1, 2020`. The `date` filter takes two parameters, the first being the date variable to be formatted and the second being the date format. The available date formats are:

- `short`: equivalent to `M/d/yy`
- `medium`: equivalent to `MMM d, yyyy`
- `long`: equivalent to `MMMM d, yyyy`
- `full`: equivalent to `EEEE, MMMM d, yyyy`

For more information on the `date` filter, see the [AngularJS documentation](https://docs.angularjs.org/api/ng/filter/date).

onelinerhub: [How can I use an AngularJS filter to format a date?](https://onelinerhub.com/angularjs/how-can-i-use-an-angularjs-filter-to-format-a-date)