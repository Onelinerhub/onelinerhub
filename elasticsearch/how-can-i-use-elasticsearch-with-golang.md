# How can I use Elasticsearch with Golang?
// plain

Elasticsearch can be used with Golang through the official [Elasticsearch Go Client](https://github.com/elastic/go-elasticsearch). This client provides an API for connecting to an Elasticsearch cluster, indexing documents, and performing searches and aggregations.

To use the Elasticsearch Go Client, first install it with the following command:
```
go get github.com/elastic/go-elasticsearch
```

Then, import the client into your Go project:
```go
import (
	"github.com/elastic/go-elasticsearch/v7"
)
```

Next, create an instance of the client:
```go
es, _ := elasticsearch.NewDefaultClient()
```

Finally, use the client to index a document:
```go
res, _ := es.Index(
	"my_index",
	strings.NewReader(`{"title": "Test Document"}`),
	es.Index.WithPretty(),
)
```

The client also provides methods for performing searches and aggregations, as well as methods for managing indexes, mappings, and aliases.

For more information, see the [Elasticsearch Go Client documentation](https://github.com/elastic/go-elasticsearch/tree/master/docs).

onelinerhub: [How can I use Elasticsearch with Golang?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-golang)