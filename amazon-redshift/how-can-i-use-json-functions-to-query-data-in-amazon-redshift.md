# How can I use JSON functions to query data in Amazon Redshift?
// plain

Using JSON functions in Amazon Redshift can be a convenient way to query data. To use JSON functions, you need to first ensure that you have the correct version of Amazon Redshift installed. The following example code block demonstrates how to use the `JSON_EXTRACT_PATH_TEXT` function to query data from a JSON document.

```
SELECT JSON_EXTRACT_PATH_TEXT(doc, 'name') AS name,
       JSON_EXTRACT_PATH_TEXT(doc, 'address.street') AS street
FROM table;
```

This code will query the `name` and `street` values from the `doc` JSON document in the `table`.

## Code explanation

- `JSON_EXTRACT_PATH_TEXT`: This is the JSON function used to extract data from a JSON document.
- `doc`: This is the JSON document from which the data will be extracted.
- `name` and `street`: These are the values that will be extracted from the JSON document.
- `table`: This is the table from which the JSON document will be retrieved.

For more information on using JSON functions in Amazon Redshift, please refer to the following links:
- [JSON Functions](https://docs.aws.amazon.com/redshift/latest/dg/JSON_FUNCTIONS.html)
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html)

onelinerhub: [How can I use JSON functions to query data in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-can-i-use-json-functions-to-query-data-in-amazon-redshift)