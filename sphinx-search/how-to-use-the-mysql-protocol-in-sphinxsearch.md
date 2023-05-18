# How to use the MySQL protocol in SphinxSearch?
// plain

SphinxSearch supports the MySQL protocol, which allows you to access the search engine using the same commands as you would use for a MySQL database. To use the MySQL protocol, you need to start the searchd daemon with the `--mysql-socket` option.

```
searchd --mysql-socket /tmp/mysql.sock
```

Once the daemon is running, you can connect to it using the `mysql` command line client.

```
mysql -S /tmp/mysql.sock
```

## Code explanation


1. Start the searchd daemon with the `--mysql-socket` option.
2. Connect to the daemon using the `mysql` command line client.
3. Execute SQL queries against the search engine.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [MySQL Protocol](http://sphinxsearch.com/docs/current.html#protocol-overview)

onelinerhub: [How to use the MySQL protocol in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-the-mysql-protocol-in-sphinxsearch)