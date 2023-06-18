# How do I connect to SphinxSearch?
// plain

To connect to SphinxSearch, you need to use the SphinxAPI. The SphinxAPI is a set of functions that allow you to connect to a Sphinx daemon and issue queries.

Below is an example of connecting to SphinxSearch using the SphinxAPI in PHP:

```
<?php
$s = new SphinxClient();
$s->setServer("localhost", 9312);
$s->setConnectTimeout(3);
$s->open();
?>
```

The code above creates a new SphinxClient object, sets the server connection parameters, and opens the connection.

The list below explains each part of the code:

- `$s = new SphinxClient();`: Creates a new SphinxClient object.
- `$s->setServer("localhost", 9312);`: Sets the host and port of the Sphinx server.
- `$s->setConnectTimeout(3);`: Sets the connection timeout in seconds.
- `$s->open();`: Opens the connection to the Sphinx server.

## Helpful links
- [SphinxAPI Documentation](http://sphinxsearch.com/docs/current.html#api-func-setconnecttimeout)
- [SphinxSearch Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-sphinx-on-ubuntu-14-04)

onelinerhub: [How do I connect to SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-connect-to-sphinxsearch)