# How do I set the maximum number of children for SphinxSearch?
// plain

Setting the maximum number of children for SphinxSearch is done by using the `max_matches` configuration option. This option determines the maximum number of matches that will be returned by a query.

## Example code

```
index myindex
{
    max_matches = 1000
}
```

The code above sets the maximum number of children for SphinxSearch to 1000.

## Code explanation


- `index myindex`: This line defines the name of the index.
- `max_matches = 1000`: This line sets the maximum number of matches that will be returned by a query to 1000.

## Helpful links

- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How do I set the maximum number of children for SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-set-the-maximum-number-of-children-for-sphinxsearch)