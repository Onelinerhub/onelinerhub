# How do I configure SphinxSearch to use binlog_flush?
// plain

SphinxSearch can be configured to use binlog_flush by setting the binlog_flush option in the Sphinx configuration file.

```
binlog_flush = 1
```

The binlog_flush option is used to flush the binlog after each indexing operation. When enabled, Sphinx will flush the binlog after each indexing operation, which ensures that the binlog is always up-to-date.

## Code explanation


* binlog_flush: This option is used to enable or disable the binlog flush feature.

List of ## Helpful links

* [SphinxSearch Documentation](https://sphinxsearch.com/docs/current.html#conf-binlog-flush)
* [SphinxSearch Binlog Flush Tutorial](https://www.tutorialspoint.com/sphinxsearch/sphinxsearch_binlog_flush.htm)

onelinerhub: [How do I configure SphinxSearch to use binlog_flush?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-sphinxsearch-to-use-binlog-flush)