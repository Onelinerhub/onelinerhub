# How do I create a view in Google Big Query?
// plain

Creating a view in Google Big Query is a simple process.

1. First, create a query that produces the desired result.

```
SELECT *
FROM [publicdata:samples.wikipedia]
```

2. Then, create a view with the query using the `CREATE VIEW` statement.

```
CREATE VIEW my_view AS
SELECT *
FROM [publicdata:samples.wikipedia]
```

3. Finally, the view can be queried as if it were a table.

```
SELECT *
FROM my_view
```

## Code explanation


* `CREATE VIEW` - the statement used to create the view
* `my_view` - the name of the view
* `SELECT *` - the query used to populate the view
* `FROM [publicdata:samples.wikipedia]` - the source table

## Helpful links

* [Google Big Query Documentation](https://cloud.google.com/bigquery/docs/)
* [Creating a View](https://cloud.google.com/bigquery/docs/views)

onelinerhub: [How do I create a view in Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-create-a-view-in-google-big-query)