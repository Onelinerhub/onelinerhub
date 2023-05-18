# How to use phrase_boundary in SphinxSearch?
// plain

SphinxSearch is a powerful full-text search engine that can be used to search for documents and other data. The phrase_boundary option allows you to specify a boundary for phrases in the search query. This can be used to ensure that only exact phrases are matched, rather than individual words.

## Example code

```
$sphinx->SetMatchMode(SPH_MATCH_PHRASE);
$sphinx->SetPhraseBoundary('.,!? ');
```

## Code explanation


- `SetMatchMode`: This function sets the matching mode for the search query. In this example, we are setting it to `SPH_MATCH_PHRASE`, which will match exact phrases instead of individual words.
- `SetPhraseBoundary`: This function sets the boundary for phrases in the search query. In this example, we are setting it to `.,!? `, which will ensure that only exact phrases are matched.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch API Reference](http://sphinxsearch.com/docs/current.html#api-reference)

onelinerhub: [How to use phrase_boundary in SphinxSearch?
](https://onelinerhub.com/sphinx-search/how-to-use-phrase_boundary-in-sphinxsearch)
