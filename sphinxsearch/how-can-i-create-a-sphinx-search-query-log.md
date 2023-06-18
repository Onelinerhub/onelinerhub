# How can I create a Sphinx search query log?
// plain

1. Create a log file for Sphinx search query by using the `searchd --log` option. This option can be used to log all queries that are sent to Sphinx.

```
searchd --log /path/to/sphinx.log
```

2. To log the query time, use the `--log-query-time` option. This will log the query time in microseconds.

```
searchd --log-query-time /path/to/sphinx.log
```

3. To log the query results, use the `--log-query-results` option. This will log the query results in JSON format.

```
searchd --log-query-results /path/to/sphinx.log
```

4. To log the query errors, use the `--log-query-errors` option. This will log the query errors in plain text format.

```
searchd --log-query-errors /path/to/sphinx.log
```

5. To log the query warnings, use the `--log-query-warnings` option. This will log the query warnings in plain text format.

```
searchd --log-query-warnings /path/to/sphinx.log
```

6. To log the query parameters, use the `--log-query-params` option. This will log the query parameters in plain text format.

```
searchd --log-query-params /path/to/sphinx.log
```

7. To log the query meta-data, use the `--log-query-meta` option. This will log the query meta-data in plain text format.

```
searchd --log-query-meta /path/to/sphinx.log
```

## Helpful links

- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
- [Sphinx Logging Options](http://sphinxsearch.com/docs/current.html#conf-log)

onelinerhub: [How can I create a Sphinx search query log?](https://onelinerhub.com/sphinxsearch/how-can-i-create-a-sphinx-search-query-log)