# How do I extract JSON data from Amazon Redshift?
// plain

### Answer

The best way to extract JSON data from Amazon Redshift is to use the `json_extract_path_text()` function. This function takes a JSON string as an argument and returns the value of the specified path.

For example, to extract the `name` field from the following JSON string:

```json
{
  "name": "John Doe",
  "age": 30
}
```

You can use the following query:

```
select json_extract_path_text('{"name": "John Doe", "age": 30}', 'name')
```

The output of this query will be:

```
John Doe
```

The `json_extract_path_text()` function can also take multiple paths as arguments, allowing you to extract multiple fields from the same JSON string.

For more information, see the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/JSON_EXTRACT_PATH_TEXT.html).

onelinerhub: [How do I extract JSON data from Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-extract-json-data-from-amazon-redshift)