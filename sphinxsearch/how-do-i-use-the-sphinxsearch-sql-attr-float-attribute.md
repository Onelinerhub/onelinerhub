# How do I use the sphinxsearch sql_attr_float attribute?
// plain

The `sql_attr_float` attribute is used within the SphinxSearch engine to define a field as a float data type. This attribute is used within the `source` block of the SphinxSearch configuration file.

For example:
```
source example_source
{
    ...

    sql_attr_float = price
    ...
}
```

In this example, the `price` field is set as a float data type.

## Code explanation


- `sql_attr_float`: This is the attribute used to define a field as a float data type.
- `price`: This is the field that is being defined as a float data type.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How do I use the sphinxsearch sql_attr_float attribute?](https://onelinerhub.com/sphinxsearch/how-do-i-use-the-sphinxsearch-sql-attr-float-attribute)