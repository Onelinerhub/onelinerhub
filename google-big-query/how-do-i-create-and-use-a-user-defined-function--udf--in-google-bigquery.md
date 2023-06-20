# How do I create and use a user-defined function (UDF) in Google BigQuery?
// plain

A user-defined function (UDF) is a type of function in Google BigQuery that allows you to write custom code in JavaScript to perform calculations on data stored in BigQuery.

To create a UDF, you must first define the function in JavaScript and then register it with BigQuery. Once registered, you can use the function in a SQL query.

For example, here is a UDF that takes a string and returns the string in uppercase:

```
CREATE TEMP FUNCTION to_uppercase(input STRING)
RETURNS STRING
LANGUAGE js AS """
  return input.toUpperCase();
""";

SELECT to_uppercase('hello world');
```

## Output example

```
HELLO WORLD
```

The code consists of the following parts:
- `CREATE TEMP FUNCTION`: This statement registers the function with BigQuery.
- `to_uppercase`: The name of the UDF.
- `input STRING`: The parameter of the UDF.
- `RETURNS STRING`: The type of the return value.
- `LANGUAGE js`: The language used for the function.
- `return input.toUpperCase();`: The code that is executed when the UDF is called.
- `SELECT to_uppercase('hello world');`: This statement calls the UDF.

For more information on creating and using UDFs in BigQuery, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions).

onelinerhub: [How do I create and use a user-defined function (UDF) in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-create-and-use-a-user-defined-function--udf--in-google-bigquery)