# How do I configure the log format for SphinxSearch?
// plain

To configure the log format for SphinxSearch, you will need to edit the configuration file. By default, the log format is set to `plain` which outputs the most basic information.

To set a custom log format, you need to add the `query_log` directive to the configuration file like this:

```
query_log = /var/log/sphinx/query.log
query_log_format = sphinxql
```

This will set the log format to `sphinxql` which will log the queries in SphinxQL format.

You can also set the log format to `sphinxql_plain` which will log queries in SphinxQL format but without the values.

The log format can also be set to `sphinxql_query` which will log only the query part of the SphinxQL statement.

You can find more information about the available log formats and how to configure them in the [SphinxSearch documentation](https://sphinxsearch.com/docs/current.html#conf-query-log-format).

## Code explanation
**

* `query_log` - Sets the path to the query log file
* `query_log_format` - Sets the log format for the query log file

**## Helpful links**

* [SphinxSearch documentation](https://sphinxsearch.com/docs/current.html#conf-query-log-format)

onelinerhub: [How do I configure the log format for SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-the-log-format-for-sphinxsearch)