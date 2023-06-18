# How can I adjust the persistent connections limit in SphinxSearch?
// plain

The persistent connections limit in SphinxSearch can be adjusted in the configuration file.

The configuration file can be found in the `/etc/sphinxsearch/sphinx.conf` directory.

In the configuration file, the `max_children` parameter can be adjusted to set the persistent connection limit. For example, to set the limit to 10, the following code can be added to the configuration file:
```
max_children = 10
```

The parts of the code and their functions are as follows:
- `max_children`: Sets the persistent connection limit
- `=`: Assigns the value to the parameter
- `10`: The value being assigned to the parameter

For more information, please refer to the [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How can I adjust the persistent connections limit in SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-can-i-adjust-the-persistent-connections-limit-in-sphinxsearch)