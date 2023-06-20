# How can I determine the length of a string in Google BigQuery?
// plain

The length of a string in Google BigQuery can be determined using the LENGTH function. This function takes a single string argument, and returns an integer value representing the length of the string.

For example, to determine the length of the string "Hello World!", the following code could be used:

```
SELECT LENGTH('Hello World!')
```

The output of this query would be 12, since the string contains 12 characters.

## Code explanation


- SELECT: This is the keyword used to initiate a query.
- LENGTH(): This is the function used to determine the length of a string.
- 'Hello World!': This is the string argument passed to the LENGTH function.

## Helpful links

- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)

onelinerhub: [How can I determine the length of a string in Google BigQuery?](https://onelinerhub.com/google-big-query/how-can-i-determine-the-length-of-a-string-in-google-bigquery)