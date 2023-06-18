# How can I use the proximity_bm25 feature in Sphinx Search?
// plain

The proximity_bm25 feature in Sphinx Search is used to boost the relevance of documents that contain words close to each other. It works by giving a higher weight to documents that have words near each other in the text, compared to documents that have the same words but with a large gap between them.

To use the proximity_bm25 feature in Sphinx Search, you need to set the `ranker` option to `proximity_bm25` when running your query. For example:

```
$query->setQuery('hello world');
$query->setRanker(SPH_RANK_PROXIMITY_BM25);
```

The output of this query will be documents where the words “hello” and “world” are close to each other, and will be ranked higher than documents where the words are far apart.

## Code explanation


- `$query->setQuery('hello world');` - This sets the query string to “hello world”.
- `$query->setRanker(SPH_RANK_PROXIMITY_BM25);` - This sets the ranker to proximity_bm25, so that documents with close words will be ranked higher.

Here are some ## Helpful links

- [Sphinx Search Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch Proximity Ranking](http://sphinxsearch.com/docs/current.html#extended-syntax-proximity-ranking)

onelinerhub: [How can I use the proximity_bm25 feature in Sphinx Search?](https://onelinerhub.com/sphinxsearch/how-can-i-use-the-proximity-bm---feature-in-sphinx-search)