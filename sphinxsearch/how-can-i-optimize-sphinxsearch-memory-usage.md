# How can I optimize sphinxsearch memory usage?
// plain

1. Reduce the number of indexes: The more indexes you have, the more memory SphinxSearch will need. Try to combine multiple indexes into one if possible.

2. Use the `max_matches` parameter: This parameter limits the amount of matches SphinxSearch can return in one query. This can help to reduce memory usage.

3. Use the `max_query_time` parameter: This parameter limits the amount of time SphinxSearch will spend searching for matches. This can help to reduce memory usage.

4. Use the `max_predicted_time` parameter: This parameter limits the amount of time SphinxSearch will spend predicting matches. This can help to reduce memory usage.

5. Use the `max_filter_values` parameter: This parameter limits the amount of values SphinxSearch can use in a filter. This can help to reduce memory usage.

6. Use the `max_filter_ratio` parameter: This parameter limits the amount of values SphinxSearch can use in a filter compared to the total number of matches. This can help to reduce memory usage.

7. Use the `max_clause_count` parameter: This parameter limits the number of clauses SphinxSearch can use in a query. This can help to reduce memory usage.

## Example code

```
searchd --max_matches=1000 --max_query_time=1000 --max_predicted_time=1000 --max_filter_values=1000 --max_filter_ratio=0.1 --max_clause_count=1000
```
No output.

onelinerhub: [How can I optimize sphinxsearch memory usage?](https://onelinerhub.com/sphinxsearch/how-can-i-optimize-sphinxsearch-memory-usage)