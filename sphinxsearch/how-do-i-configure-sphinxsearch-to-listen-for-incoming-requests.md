# How do I configure SphinxSearch to listen for incoming requests?
// plain

To configure SphinxSearch to listen for incoming requests, you need to specify an address and port for it to bind to. This can be done by adding the `listen` directive to the Sphinx configuration file.

For example, to configure Sphinx to listen on `127.0.0.1` port `9312`:

```
listen = 127.0.0.1:9312
```

You may also need to configure Sphinx to listen on `0.0.0.0` if you want to make it accessible from other machines.

If you have multiple searchd instances, you can specify different ports for each instance.

You may also need to configure Sphinx to listen on a Unix socket. This can be done by specifying a path for the socket in the `listen` directive.

```
listen = /var/run/sphinx.sock
```

Once you have configured Sphinx to listen for incoming requests, you can start the searchd daemon with the `searchd` command.

## Helpful links

- [Sphinx Documentation - listen Directive](https://sphinxsearch.com/docs/current.html#conf-listen)
- [Sphinx Documentation - searchd Command](https://sphinxsearch.com/docs/current.html#searchd)

onelinerhub: [How do I configure SphinxSearch to listen for incoming requests?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-sphinxsearch-to-listen-for-incoming-requests)