# How can I delete documents from my Elasticsearch index using the delete by query API?
// plain

Using the delete by query API, you can delete documents from an Elasticsearch index. The API takes a query in the form of a JSON object and uses it to select documents that should be deleted.

## Example code


```
DELETE /index_name/_delete_by_query
{
  "query": {
    "match_all": {}
  }
}
```

The above code will delete all documents from the index called `index_name`.

The query object can be used to specify more specific conditions for which documents should be deleted. For example, the following code will delete all documents with the field `title` equal to `My Document`:

```
DELETE /index_name/_delete_by_query
{
  "query": {
    "match": {
      "title": "My Document"
    }
  }
}
```

The delete by query API also supports more advanced query types such as range queries and wildcard queries.

## Code explanation


1. `DELETE /index_name/_delete_by_query` - This is the API call used to delete documents from an Elasticsearch index.
2. `{ "query": { "match_all": {} } }` - This is the query object used to select which documents should be deleted.
3. `{ "query": { "match": { "title": "My Document" } } }` - This is an example of a more specific query object used to delete documents with the field `title` equal to `My Document`.

## Helpful links

- [Elasticsearch Delete By Query API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-delete-by-query.html)
- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

onelinerhub: [How can I delete documents from my Elasticsearch index using the delete by query API?](https://onelinerhub.com/elasticsearch/how-can-i-delete-documents-from-my-elasticsearch-index-using-the-delete-by-query-api)