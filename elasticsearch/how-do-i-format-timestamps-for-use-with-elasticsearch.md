# How do I format timestamps for use with Elasticsearch?
// plain

The Elasticsearch Timestamp datatype is used to index and store date and time values. It is stored in the format of an epoch, which is a Unix-style timestamp, and is used to represent the number of milliseconds since January 1, 1970. To format timestamps for use with Elasticsearch, you can use the `Date.getTime()` function in JavaScript to convert a Date object to an epoch timestamp.

For example:

```
let date = new Date();
let epoch = date.getTime();
console.log(epoch);
```

## Output example

```
1607817243737
```

The above code creates a new `Date` object, and then uses the `getTime()` function to convert it to an epoch timestamp.

You can also use the `Date.parse()` function to convert a string representation of a date to an epoch timestamp. For example:

```
let dateString = '2021-01-01';
let epoch = Date.parse(dateString);
console.log(epoch);
```

## Output example

```
1609459200000
```

The above code uses the `Date.parse()` function to convert the string '2021-01-01' to an epoch timestamp.

You can find more information about formatting timestamps for use with Elasticsearch in the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/date.html).

onelinerhub: [How do I format timestamps for use with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-format-timestamps-for-use-with-elasticsearch)