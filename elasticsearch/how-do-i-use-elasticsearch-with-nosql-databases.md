# How do I use Elasticsearch with NoSQL databases?
// plain

Elasticsearch can be used with NoSQL databases by creating an index that references the documents stored in the NoSQL database. This index can then be used to query the documents in the NoSQL database using the Elasticsearch Query DSL.

For example, if you have a MongoDB database with documents stored as JSON strings, you can create an index in Elasticsearch that references the documents in MongoDB.

```
PUT /index_name
{
  "mappings": {
    "properties": {
      "mongo_id": {
        "type": "keyword"
      },
      "name": {
        "type": "text"
      },
      "age": {
        "type": "integer"
      }
    }
  }
}
```

The above example creates an index in Elasticsearch with three fields - `mongo_id` (which is a keyword field type), `name` (which is a text field type), and `age` (which is an integer field type).

Now that we have an index in Elasticsearch, we can query the documents in MongoDB using the Elasticsearch Query DSL. For example, if we wanted to find all documents in MongoDB with a `name` field equal to "John", we could use the following query:

```
GET /index_name/_search
{
  "query": {
    "match": {
      "name": "John"
    }
  }
}
```

The above query will return all documents in MongoDB with a `name` field equal to "John".

## Helpful links

- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
- [MongoDB](https://www.mongodb.com/)
- [Elasticsearch](https://www.elastic.co/products/elasticsearch)

onelinerhub: [How do I use Elasticsearch with NoSQL databases?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-with-nosql-databases)