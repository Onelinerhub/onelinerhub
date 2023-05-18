# How to use custom ranker in SphinxSearch?
// plain

Using custom ranker in SphinxSearch is a powerful way to customize the relevance of search results.

To use custom ranker, you need to define a custom ranker function in your Sphinx configuration file.

```
ranker = custom
custom_ranker = expr:sum(lcs*user_weight1 + bm25*user_weight2)
```

The above code defines a custom ranker function that combines two ranking algorithms, Longest Common Subsequence (LCS) and BM25. The user_weight1 and user_weight2 parameters can be adjusted to customize the relevance of the search results.

The parts of the code are:
- `ranker = custom`: This line tells Sphinx to use a custom ranker.
- `custom_ranker = expr:sum(lcs*user_weight1 + bm25*user_weight2)`: This line defines the custom ranker function. The `lcs` and `bm25` parameters are ranking algorithms, and the `user_weight1` and `user_weight2` parameters can be adjusted to customize the relevance of the search results.

## Helpful links
- [Sphinx Documentation - Custom Ranking](http://sphinxsearch.com/docs/current.html#conf-ranker)

onelinerhub: [How to use custom ranker in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-custom-ranker-in-sphinxsearch)