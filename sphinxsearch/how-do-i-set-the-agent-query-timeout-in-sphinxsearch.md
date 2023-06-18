# How do I set the agent query timeout in Sphinxsearch?
// plain

In order to set the agent query timeout in SphinxSearch, you need to set the `query_timeout` option in the `searchd` configuration. This option specifies the timeout in seconds for the query processing.

For example, to set the timeout to 10 seconds, the following configuration should be used:
```
searchd {
  ...
  query_timeout = 10
  ...
}
```

The configuration can be applied with the `searchd` command.

Relevant parts:
- `query_timeout`: option that specifies the timeout in seconds for the query processing

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How do I set the agent query timeout in Sphinxsearch?](https://onelinerhub.com/sphinxsearch/how-do-i-set-the-agent-query-timeout-in-sphinxsearch)