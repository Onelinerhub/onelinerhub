# How can I use Elasticsearch KNN to find similar documents?
// plain

K Nearest Neighbors (KNN) is a machine learning algorithm used for finding similar documents in an Elasticsearch index. It works by computing the similarity between documents using a distance metric such as Euclidean or cosine distance. The algorithm then returns the K nearest neighbors to a given document.

## Example code

```
GET /my_index/_search
{
  "query": {
    "knn": {
      "my_field": {
        "vector": [1,2,3],
        "k": 10
      }
    }
  }
}
```

This example code searches the index `my_index` for documents similar to the given vector [1,2,3], and returns the 10 nearest neighbors.

The code consists of several parts:

1. The `GET` command which specifies the index to search.
2. The `query` section, which contains the `knn` query with the `my_field` field containing the vector to search, and the `k` parameter specifying the number of nearest neighbors to return.

For more information on using KNN in Elasticsearch, please refer to the [Elasticsearch KNN documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn.html).

onelinerhub: [How can I use Elasticsearch KNN to find similar documents?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-knn-to-find-similar-documents)