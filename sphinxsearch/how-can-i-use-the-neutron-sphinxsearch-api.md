# How can I use the Neutron/SphinxSearch API?
// plain

The Neutron/SphinxSearch API is an open source search engine that can be used to quickly and easily search a variety of data sources. It provides a powerful and flexible API for building search applications.

The API is easy to use and provides a number of methods for searching data. For example, a search query can be constructed using the `query()` method. This method takes a string representing the search query as its only argument and returns an array of results.

```
// Example code
$results = $sphinx->query('search query');
```

The `fetch()` method can be used to retrieve the results of a search query. It takes an array of document IDs as its only argument and returns an array of documents.

```
// Example code
$documents = $sphinx->fetch($results);
```

The `filter()` method can be used to filter the results of a search query. It takes an array of filters as its only argument and returns an array of documents that match the specified criteria.

```
// Example code
$filtered_results = $sphinx->filter($filters);
```

The `sort()` method can be used to sort the results of a search query. It takes an array of sorting criteria as its only argument and returns an array of documents sorted according to the specified criteria.

```
// Example code
$sorted_results = $sphinx->sort($sort_criteria);
```

The Neutron/SphinxSearch API provides a powerful and flexible way to search data sources. It is easy to use and provides a number of methods for constructing search queries and manipulating the results.

## Helpful links
- [Neutron/SphinxSearch Documentation](https://neutron.readthedocs.io/en/latest/sphinxsearch.html)
- [Neutron/SphinxSearch API Reference](https://neutron.readthedocs.io/en/latest/api/sphinxsearch.html)

onelinerhub: [How can I use the Neutron/SphinxSearch API?](https://onelinerhub.com/sphinxsearch/how-can-i-use-the-neutron-sphinxsearch-api)