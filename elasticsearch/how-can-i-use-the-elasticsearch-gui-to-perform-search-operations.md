# How can I use the Elasticsearch GUI to perform search operations?
// plain

Elasticsearch provides a graphical user interface (GUI) for performing search operations. To use the GUI, first open the browser and go to the URL of the Elasticsearch instance.

The GUI provides a search bar to enter a query. For example, the following query will return all documents in the `my_index` index:

```
GET my_index/_search
```

The query can also include parameters to filter and sort the results, such as the following:

```
GET my_index/_search
{
  "query": {
    "match": {
      "title": "Elasticsearch"
    }
  },
  "sort": [
    {
      "date": {
        "order": "desc"
      }
    }
  ]
}
```

The output of the query will be a JSON object containing the search results.

The GUI also provides various options to customize the search query, such as adding filters and aggregations.

The GUI also allows users to save queries and view their history.

For more information about using the Elasticsearch GUI, see the [official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-body.html).

onelinerhub: [How can I use the Elasticsearch GUI to perform search operations?](https://onelinerhub.com/elasticsearch/how-can-i-use-the-elasticsearch-gui-to-perform-search-operations)