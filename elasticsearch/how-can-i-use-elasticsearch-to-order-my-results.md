# How can I use Elasticsearch to order my results?
// plain

Elasticsearch offers a powerful way to order search results. It can be used to sort results based on relevance, date, or any other field.

For example, to order results by relevance, you can use the following code:
```
GET /_search
{
  "query": {
    "match": {
      "title": "elasticsearch"
    }
  },
  "sort": [
    {
      "_score": {
        "order": "desc"
      }
    }
  ]
}
```
The output of the above code will be sorted by relevance, with the most relevant results appearing first.

To order results by date, you can use the following code:
```
GET /_search
{
  "query": {
    "match": {
      "title": "elasticsearch"
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
The output of the above code will be sorted by date, with the most recent results appearing first.

## Code explanation

- `GET /_search`: the request to search for documents
- `query`: the query to use to search for documents
- `sort`: the field to use to sort the results
- `_score`: the relevance of the document to the query
- `date`: the date of the document
- `order`: the order to sort the results (ascending or descending)

## Helpful links
- [Elasticsearch Reference: Sorting](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-sort.html)
- [Elasticsearch Reference: Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

onelinerhub: [How can I use Elasticsearch to order my results?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-to-order-my-results)