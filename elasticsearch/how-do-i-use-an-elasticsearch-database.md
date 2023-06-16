# How do I use an elasticsearch database?
// plain

Elasticsearch is a distributed, open source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. To use an elasticsearch database, first you need to install it. You can find the installation instructions [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html).

Once you have installed elasticsearch, you can start using it. For example, you can use the following code to index a document:

```
PUT my_index
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text"
      },
      "body": {
        "type": "text"
      }
    }
  }
}
```

This code creates an index called `my_index` with two fields `title` and `body`. You can then add documents to the index using `POST` requests:

```
POST my_index/_doc/1
{
  "title": "My first document",
  "body": "This is the content of my first document"
}
```

This code adds a document with an ID of `1` and the specified `title` and `body` fields. You can then search the index using `GET` requests:

```
GET my_index/_search
{
  "query": {
    "match": {
      "title": "first"
    }
  }
}
```

This code searches the index for documents with a `title` field containing the word `first`. The output of this query will be a list of documents matching the search criteria.

You can find more information about using elasticsearch in the [official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).

onelinerhub: [How do I use an elasticsearch database?](https://onelinerhub.com/elasticsearch/how-do-i-use-an-elasticsearch-database)