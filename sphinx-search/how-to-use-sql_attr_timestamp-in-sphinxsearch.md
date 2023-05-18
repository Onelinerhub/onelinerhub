# How to use sql_attr_timestamp in SphinxSearch?
// plain

SphinxSearch provides the `sql_attr_timestamp` directive to index and query timestamp fields. This directive allows Sphinx to convert a timestamp field into a UNIX timestamp, which can then be used for sorting and filtering.

## Example code

```
index test
{
    source = test_source
    sql_attr_timestamp = timestamp_field
}
```

This example code will index the `timestamp_field` from the `test_source` source.

## Code explanation

- `index test`: This defines the index name.
- `source = test_source`: This defines the source from which the data will be indexed.
- `sql_attr_timestamp = timestamp_field`: This directive tells Sphinx to convert the `timestamp_field` from the `test_source` source into a UNIX timestamp.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [sql_attr_timestamp Directive](http://sphinxsearch.com/docs/current.html#conf-sql-attr-timestamp)

onelinerhub: [How to use sql_attr_timestamp in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-sql_attr_timestamp-in-sphinxsearch)