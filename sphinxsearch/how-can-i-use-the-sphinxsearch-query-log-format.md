# How can I use the SphinxSearch query_log_format?
// plain

The SphinxSearch query_log_format is a tool that allows you to log queries to a file. It can be used to track query performance, diagnose query problems, and analyze query trends.

To use the query_log_format, you must first enable logging in the Sphinx configuration file. You can do this by adding the following line to the configuration file:

```
query_log_format = json
```

Once logging is enabled, you can write queries to the log file using the following command:

```
indexer --querylog <log_file_name> <index_name>
```

The --querylog flag indicates that queries should be logged to the specified log file. The log file will contain a JSON-formatted log of each query that was run against the specified index.

The log file will contain data such as the query string, the query time, the query results, and any errors that occurred while running the query. This data can be used to analyze query performance, diagnose query problems, and track query trends.

For more information on the query_log_format, see the [SphinxSearch Documentation](https://sphinxsearch.com/docs/current.html#query-logging).

onelinerhub: [How can I use the SphinxSearch query_log_format?](https://onelinerhub.com/sphinxsearch/how-can-i-use-the-sphinxsearch-query-log-format)