# How do I use Elasticsearch to sort data?
// plain

Elasticsearch can be used to sort data in a variety of ways. To sort data, you need to create an index, specify the data type, and then use the sort API.

For example, the following code block will create an index called “my_index”, specify the data type as “string”, and then sort the data by the “name” field in ascending order:

```
PUT my_index
{
  "mappings": {
    "properties": {
      "name": {
        "type": "string"
      }
    }
  }
}

POST my_index/_search
{
  "sort": [
    {
      "name": {
        "order": "asc"
      }
    }
  ]
}
```

The output of the above code will be a JSON response containing the sorted data.

## Code explanation

1. `PUT my_index` - Creates an index called “my_index”.
2. `"type": "string"` - Specifies the data type as “string”.
3. `"name": { "order": "asc" }` - Sorts the data by the “name” field in ascending order.
4. `POST my_index/_search` - Executes the search.

## Helpful links
- [Elasticsearch Documentation - Sorting](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-sort.html)
- [Elasticsearch Documentation - Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)

onelinerhub: [How do I use Elasticsearch to sort data?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-to-sort-data)