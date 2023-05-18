# How to use sql_attr_json in SphinxSearch?
// plain

SphinxSearch supports the `sql_attr_json` directive to index JSON data stored in a database. This directive allows Sphinx to index the data as a single attribute, which can then be used in queries.

## Example code

```
sql_attr_json = json_data
```

This code will index the `json_data` column in the database as a single attribute.

## Code explanation


- `sql_attr_json`: This directive tells Sphinx to index the data as a single attribute.
- `json_data`: This is the name of the column in the database that contains the JSON data.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How to use sql_attr_json in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-sql_attr_json-in-sphinxsearch)