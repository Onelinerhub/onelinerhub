# How can I join two Elasticsearch indices?
// plain

Joining two Elasticsearch indices is possible by using the [`search_after`](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-search-after.html) parameter. It allows you to search for documents after a certain document. The following example code block shows how to join two indices:

```ruby
# First search
response1 = Elasticsearch::Client.search index: 'index1', body: {
  query: {
    match: {
      field1: 'value1'
    }
  },
  sort: [
    {
      _id: 'asc'
    }
  ]
}

# Second search
response2 = Elasticsearch::Client.search index: 'index2', body: {
  query: {
    match: {
      field2: 'value2'
    }
  },
  search_after: response1['hits']['hits'].last['_id']
}
```

This will return the documents from the first index (`index1`) sorted by the `_id` field, and then the documents from the second index (`index2`) sorted by the `_id` field after the last document from the first index.

Parts of the code explained:

* `response1`: The first search request which searches for documents in `index1` and sorts them by the `_id` field.
* `response2`: The second search request which searches for documents in `index2` and sorts them by the `_id` field after the last document from `index1`. The `search_after` parameter is used here to specify the last document from `index1`.
* `response1['hits']['hits'].last['_id']`: This is used to get the `_id` of the last document from `index1` which is used as the `search_after` parameter in the second search request.

## Helpful links

* [Elasticsearch search_after parameter](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-search-after.html)
* [Elasticsearch Client](https://www.elastic.co/guide/en/elasticsearch/client/ruby-api/current/index.html)

onelinerhub: [How can I join two Elasticsearch indices?](https://onelinerhub.com/elasticsearch/how-can-i-join-two-elasticsearch-indices)