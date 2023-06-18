# How can I format a date in ReactJS?
// plain

ReactJS provides the `Date()` constructor to format dates. You can use the `toLocaleDateString()` method to format the date in a specified locale.

For example:
```
let date = new Date();
let formattedDate = date.toLocaleDateString();
console.log(formattedDate); // output: "6/19/2020"
```

The `toLocaleDateString()` method takes two optional arguments:

- `locales`: A string with a BCP 47 language tag, or an array of such strings. This will determine the language in which the date is formatted.
- `options`: An object with some or all of the following options:
  - `weekday`: The representation of the weekday. Possible values are "narrow", "short" or "long".
  - `year`: The representation of the year. Possible values are "numeric" or "2-digit".
  - `month`: The representation of the month. Possible values are "numeric", "2-digit", "narrow", "short" or "long".
  - `day`: The representation of the day. Possible values are "numeric" or "2-digit".

For example:
```
let date = new Date();
let formattedDate = date.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
console.log(formattedDate); // output: "June 19, 2020"
```

React also provides the `format()` method in [date-fns](https://date-fns.org/v2.16.1/docs/format) to format dates. It takes two arguments:

- `date`: A Date object or anything that can be passed to the `Date()` constructor.
- `formatString`: A string of tokens that indicates how to format the date.

For example:
```
import { format } from 'date-fns';

let date = new Date();
let formattedDate = format(date, 'MMMM do, yyyy');
console.log(formattedDate); // output: "June 19th, 2020"
```

React also provides the `Intl.DateTimeFormat()` constructor to format dates. It takes an optional `options` object with the same options as the `toLocaleDateString()` method.

For example:
```
let date = new Date();
let formattedDate = new Intl.DateTimeFormat('en-US', { month: 'long', day: 'numeric', year: 'numeric' }).format(date);
console.log(formattedDate); // output: "June 19, 2020"
```

React also provides the `formatRelative()` method in [date-fns](https://date-fns.org/v2.16.1/docs/formatRelative) to format dates relative to a given base date. It takes two arguments:

- `date`: A Date object or anything that can be passed to the `Date()` constructor.
- `baseDate`: A Date object or anything that can be passed to the `Date()` constructor.

For example:
```
import { formatRelative } from 'date-fns';

let date = new Date();
let baseDate = new Date(2020, 5, 14);
let formattedDate = formatRelative(date, baseDate);
console.log(formattedDate); // output: "5 days ago"
```

## Helpful links

- [Date.prototype.toLocaleDateString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString)
- [date-fns - format](https://date-fns.org/v2.16.1/docs/format)
- [Intl.DateTimeFormat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DateTimeFormat)
- [date-fns - formatRelative](https://date-fns.org/v2.16.1/docs/formatRelative)

onelinerhub: [How can I format a date in ReactJS?](https://onelinerhub.com/reactjs/how-can-i-format-a-date-in-reactjs)