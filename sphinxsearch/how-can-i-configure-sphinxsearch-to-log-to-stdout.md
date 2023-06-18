# How can I configure SphinxSearch to log to stdout?
// plain

SphinxSearch can be configured to log to stdout with the following steps:

1. Open `sphinx.conf` in a text editor.
2. Find the `searchd` section and add the following line:
    ```
    log = stdout
    ```
3. Save and close `sphinx.conf`.
4. Restart SphinxSearch with the `--config` option, e.g. `searchd --config /etc/sphinx/sphinx.conf`.

The output will then be written to stdout, e.g.
```
[Fri Jan 31 15:06:45.890 2020] [0] listening on all interfaces, port=9312
[Fri Jan 31 15:06:45.890 2020] [0] listening on all interfaces, port=9306
[Fri Jan 31 15:06:45.890 2020] [0] listening on all interfaces, port=9308
[Fri Jan 31 15:06:45.890 2020] [0] listening on all interfaces, port=9315
[Fri Jan 31 15:06:45.890 2020] [0] listening on all interfaces, port=9313
[Fri Jan 31 15:06:45.890 2020] [0] listening on all interfaces, port=9309
```

For more information, see the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How can I configure SphinxSearch to log to stdout?](https://onelinerhub.com/sphinxsearch/how-can-i-configure-sphinxsearch-to-log-to-stdout)