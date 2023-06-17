# How can I use the Elasticsearch web UI to search my data?
// plain

The Elasticsearch web UI is a great tool for searching and exploring data. Here's how to use it:

1. Log in to the Elasticsearch web UI.
2. In the "Index" field, enter the name of the index you want to search.
3. In the query box, enter your search query. You can use the [Lucene query syntax](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html) to search for specific terms or phrases.
4. Click the "Search" button to submit your query.
5. The results will be displayed in the "Results" section.
6. You can use the filters on the left side of the page to narrow down your search results.
7. To view a specific document, click on its ID in the "Results" section.

## Example code


```
GET /my_index/_search
{
  "query": {
    "match": {
      "field_name": "my_search_term"
    }
  }
}
```

## Output example


```
{
  "took": 5,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 0.2876821,
    "hits": [
      {
        "_index": "my_index",
        "_type": "_doc",
        "_id": "1",
        "_score": 0.2876821,
        "_source": {
          "field_name": "my_search_term"
        }
      }
    ]
  }
}
```

The code above searches the index "my_index" for documents containing the term "my_search_term" in the "field_name" field. The output shows that one document was found and its ID is "1".

onelinerhub: [How can I use the Elasticsearch web UI to search my data?](https://onelinerhub.com/elasticsearch/how-can-i-use-the-elasticsearch-web-ui-to-search-my-data)