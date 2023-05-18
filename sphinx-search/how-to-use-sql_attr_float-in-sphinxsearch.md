# How to use sql_attr_float in SphinxSearch?
// plain

SphinxSearch provides the `sql_attr_float` directive to index and search float values. This directive is used to define a float attribute in the index.

## Example code

```
index test1
{
    source          = src1
    sql_attr_float  = price
}
```

The above code defines a float attribute named `price` in the index `test1`.

## Code explanation


1. `index test1`: This defines the index name.
2. `source = src1`: This defines the source of the data.
3. `sql_attr_float = price`: This defines the float attribute named `price`.

## Helpful links

1. [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
2. [sql_attr_float Directive](http://sphinxsearch.com/docs/current.html#conf-sql-attr-float)

onelinerhub: [How to use sql_attr_float in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-sql_attr_float-in-sphinxsearch)