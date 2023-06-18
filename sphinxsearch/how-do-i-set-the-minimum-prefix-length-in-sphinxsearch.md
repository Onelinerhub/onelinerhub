# How do I set the minimum prefix length in SphinxSearch?
// plain

To set the minimum prefix length in SphinxSearch, you need to use the `min_prefix_len` option. This option defines the minimum length of a word to be indexed as a prefix.

For example, to set the prefix length to 3:
```
index myindex
{
    ...
    min_prefix_len = 3
    ...
}
```

## Code explanation


- `index` - defines the name of the index
- `min_prefix_len` - sets the minimum prefix length

For more information, see the [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I set the minimum prefix length in SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-set-the-minimum-prefix-length-in-sphinxsearch)