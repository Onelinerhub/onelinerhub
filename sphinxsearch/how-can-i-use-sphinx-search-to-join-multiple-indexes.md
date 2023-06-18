# How can I use Sphinx Search to join multiple indexes?
// plain

Sphinx Search can be used to join multiple indexes by using its distributed indexes feature. This feature allows a single search query to be executed across multiple indexes.

For example, the following code will join two indexes, `index_a` and `index_b`:
```
SELECT * FROM index_a
JOIN index_b
USING (id)
```

The code consists of the following parts:
1. `SELECT *` - this will return all columns from the joined indexes.
2. `FROM index_a` - this is the first index to be joined.
3. `JOIN index_b` - this is the second index to be joined.
4. `USING (id)` - this is the column to be used for the join.

For more information on distributed indexes, please see the [Sphinx documentation](https://sphinxsearch.com/docs/current.html#distributed-indexes).

onelinerhub: [How can I use Sphinx Search to join multiple indexes?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinx-search-to-join-multiple-indexes)