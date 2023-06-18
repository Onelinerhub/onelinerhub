# How do I set the client_timeout for sphinxsearch?
// plain

The client_timeout setting for Sphinxsearch is used to control the maximum amount of time a client can wait for a response from the searchd server.

To set the client_timeout, you can use the `set_connect_timeout()` function in the PHP API. The following example code block shows how to set the timeout to 10 seconds:

```
$cl->set_connect_timeout(10);
```

The `set_connect_timeout()` function takes a single parameter, which is the timeout in seconds.

In addition to the `set_connect_timeout()` function, you can also set the client_timeout in the Sphinx configuration file (sphinx.conf). The following example shows how to set the client_timeout to 15 seconds in the configuration file:

```
client_timeout = 15
```

Once the client_timeout is set, it will remain in effect until it is changed again.

## Code explanation
**
- `set_connect_timeout()`: function used to set the timeout in seconds
- `client_timeout`: setting used to control the maximum amount of time a client can wait for a response from the searchd server

**## Helpful links**
- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
- [Sphinx PHP API Documentation](http://sphinxsearch.com/docs/current.html#api-func-set-connect-timeout)

onelinerhub: [How do I set the client_timeout for sphinxsearch?](https://onelinerhub.com/sphinxsearch/how-do-i-set-the-client-timeout-for-sphinxsearch)