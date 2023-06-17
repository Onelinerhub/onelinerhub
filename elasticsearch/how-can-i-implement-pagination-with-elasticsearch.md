# How can I implement pagination with Elasticsearch?
// plain

Pagination with Elasticsearch can be implemented with the `from` and `size` parameters. The `from` parameter specifies the offset from the first result you want to fetch, and the `size` parameter specifies how many results you want to fetch.

For example, to fetch the second page of results with 10 results per page, you can use the following code:

```
GET /_search
{
  "from": 10,
  "size": 10
}
```

The output will be 10 results starting from the 11th result.

## Code explanation

- `GET /_search`: This is the endpoint for searching documents in Elasticsearch.
- `from`: This parameter specifies the offset from the first result you want to fetch.
- `size`: This parameter specifies how many results you want to fetch.
- `10`: This is the value of the `from` parameter, indicating that the results should start from the 11th result.
- `10`: This is the value of the `size` parameter, indicating that 10 results should be returned.

## Helpful links
- [Elasticsearch Pagination](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-from-size.html)

onelinerhub: [How can I implement pagination with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-implement-pagination-with-elasticsearch)