# How can I use SphinxSearch attributes to optimize my search results?
// plain

SphinxSearch is a powerful full-text search engine that can be used to optimize search results. It uses attributes to help refine and prioritize search results. Here is an example of how to use attributes to optimize search results:

```
$cl->SetMatchMode(SPH_MATCH_EXTENDED);
$cl->SetSortMode(SPH_SORT_RELEVANCE, '@weight DESC');
$cl->SetFieldWeights(array('title' => 10, 'content' => 5));
```

This code sets the search engine to use the extended matching mode, which allows for more complex queries, and sets the sorting mode to prioritize results by relevance and weight. The field weights are set to give more importance to the title field than the content field.

The following list explains each part of the code:

- `SetMatchMode(SPH_MATCH_EXTENDED)`: Sets the search engine to use the extended matching mode, which allows for more complex queries.
- `SetSortMode(SPH_SORT_RELEVANCE, '@weight DESC')`: Sets the sorting mode to prioritize results by relevance and weight.
- `SetFieldWeights(array('title' => 10, 'content' => 5))`: Sets the field weights to give more importance to the title field than the content field.

By using these attributes, you can optimize your search results to give more relevant and accurate results.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch Attributes](https://www.digitalocean.com/community/tutorials/how-to-configure-sphinx-on-ubuntu-14-04)

onelinerhub: [How can I use SphinxSearch attributes to optimize my search results?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinxsearch-attributes-to-optimize-my-search-results)