# How to use regexp_filter in SphinxSearch?
// plain

Regexp_filter is a powerful feature of SphinxSearch that allows you to filter search results using regular expressions.

## Example

```
SELECT * FROM index WHERE MATCH('@title regexp_filter /^[A-Z]/')
```

## Output example

```
+------+------------+
| id   | title      |
+------+------------+
|    1 | Apple      |
|    2 | Banana     |
|    3 | Carrot     |
+------+------------+
```

## Code explanation

- SELECT * FROM index: This is the query that will be used to search the index.
- WHERE MATCH('@title regexp_filter /^[A-Z]/'): This is the regexp_filter clause that will be used to filter the search results. The regular expression used here is `/^[A-Z]/`, which will match any string that starts with an uppercase letter.
- Output: This is the output of the query, which shows only the results that match the regular expression.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use regexp_filter in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-regexp_filter-in-sphinxsearch)