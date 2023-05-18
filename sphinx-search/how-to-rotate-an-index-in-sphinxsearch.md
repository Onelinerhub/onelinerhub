# How to rotate an index in SphinxSearch?
// plain

SphinxSearch supports index rotation, which allows you to switch between two or more indexes without restarting the searchd daemon. This is useful for updating an index without interrupting the search service.

To rotate an index, use the `rotate` command in the Sphinx configuration file. For example:

```
index test1
{
    ...
    rotate = 1
}

index test2
{
    ...
    rotate = 2
}
```

This will cause the searchd daemon to switch between the two indexes every time the `rotate` command is called.

The `rotate` command has several parameters that can be used to control the rotation process. These include:

- `max_rotate_period`: The maximum time (in seconds) that the searchd daemon will wait before switching to the next index.
- `max_rotate_wait`: The maximum time (in seconds) that the searchd daemon will wait before switching to the next index.
- `rotate_period`: The time (in seconds) that the searchd daemon will wait before switching to the next index.
- `rotate_wait`: The time (in seconds) that the searchd daemon will wait before switching to the next index.

For more information, see the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html#conf-rotate).

onelinerhub: [How to rotate an index in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-rotate-an-index-in-sphinxsearch)