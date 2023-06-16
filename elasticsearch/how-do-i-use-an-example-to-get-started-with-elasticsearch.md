# How do I use an example to get started with Elasticsearch?
// plain

1. First, install Elasticsearch. You can find instructions on how to do this [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html).

2. Next, you can use the following example to get started with Elasticsearch. This example will index a document, and then search for it.

```
# Index a document
curl -XPUT 'localhost:9200/customer/external/1?pretty' -H 'Content-Type: application/json' -d'
{
  "name": "John Doe"
}
'

# Search for the document
curl -XGET 'localhost:9200/customer/external/1?pretty'
```

The output of the search should be:

```
{
  "_index" : "customer",
  "_type" : "external",
  "_id" : "1",
  "_version" : 1,
  "found" : true,
  "_source" : {
    "name" : "John Doe"
  }
}
```

3. The code above consists of two parts:
    * The first part uses the `curl -XPUT` command to index a document. This command takes the URL of the document, the content type, and the document itself as parameters.
    * The second part uses the `curl -XGET` command to search for the document. This command takes the URL of the document as a parameter.

4. To learn more about how to use Elasticsearch, please refer to the [official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).

5. You can also find more examples and tutorials [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html).

6. Finally, you can use the [Elasticsearch API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs.html) to explore the different operations you can perform with Elasticsearch.

7. With this example, you should now have a basic understanding of how to get started with Elasticsearch.

onelinerhub: [How do I use an example to get started with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-use-an-example-to-get-started-with-elasticsearch)