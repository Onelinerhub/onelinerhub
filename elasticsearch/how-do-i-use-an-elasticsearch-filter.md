# How do I use an elasticsearch filter?
// plain

An Elasticsearch filter is a query that is used to limit the search results within a specific index or type. It can be used to filter out documents that do not match a certain criteria.

For example, the following code block can be used to filter out documents with a field called "status" that is not equal to "published":

```
GET /my_index/_search
{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "status": "published"
        }
      }
    }
  }
}
```

The code block consists of the following parts:

- `GET /my_index/_search`: This is the request URL which specifies the index to search.

- `query`: This is the query object which contains the filter.

- `bool`: This is the boolean query which allows for combining multiple queries.

- `filter`: This is the filter object which contains the criteria for filtering the documents.

- `term`: This is the term query which is used to match the specific field of the document.

- `status`: This is the field name which is used to filter the documents.

- `published`: This is the value which is used to filter out the documents that do not match the criteria.

For more information on using Elasticsearch filters, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-filter.html).

onelinerhub: [How do I use an elasticsearch filter?](https://onelinerhub.com/elasticsearch/how-do-i-use-an-elasticsearch-filter)