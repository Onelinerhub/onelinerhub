# How can I use Elasticsearch with C#?
// plain

Elasticsearch can be used with C# via the official low-level client library [NEST](https://www.elastic.co/guide/en/elasticsearch/client/net-api/current/introduction.html).

NEST provides a strongly-typed query DSL that maps 1:1 with the Elasticsearch query DSL, and takes advantage of specific C# features such as covariant results and auto mapping of POCO types.

Example code to connect to an Elasticsearch cluster, index a document, and search for it:

```csharp
var defaultIndex = "my-index";

var settings = new ConnectionSettings(new Uri("http://localhost:9200"))
    .DefaultIndex(defaultIndex);

var client = new ElasticClient(settings);

// Index a document
var person = new Person { Id = 1, Name = "Martijn Laarman" };
var indexResponse = client.IndexDocument(person);

// Search for the document
var searchResponse = client.Search<Person>(s => s
    .Query(q => q
        .Term(f => f.Name, person.Name)
    )
);

// Output the total number of documents found
Console.WriteLine($"{searchResponse.Total} documents found");
```

## Output example

```
1 documents found
```

The code above does the following:
1. Creates a `ConnectionSettings` object, which specifies the connection parameters to the Elasticsearch cluster.
2. Creates an `ElasticClient` object, using the `ConnectionSettings`.
3. Indexes a `Person` object, which is a custom POCO type.
4. Searches for the document using a `Term` query on the `Name` field.
5. Outputs the total number of documents found.

## Helpful links
- [NEST Homepage](https://www.elastic.co/guide/en/elasticsearch/client/net-api/current/introduction.html)
- [NEST Documentation](https://www.elastic.co/guide/en/elasticsearch/client/net-api/current/index.html)
- [NEST GitHub Repository](https://github.com/elastic/elasticsearch-net)

onelinerhub: [How can I use Elasticsearch with C#?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-c-)