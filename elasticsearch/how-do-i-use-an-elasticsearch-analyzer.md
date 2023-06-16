# How do I use an Elasticsearch analyzer?
// plain

An Elasticsearch analyzer is a combination of one tokenizer and zero or more token filters that are used to break a string down into tokens.

To use an analyzer, you can define a custom analyzer in the mapping of an index, or use one of the built-in analyzers.

For example, to create a custom analyzer with a whitespace tokenizer and lowercase filter, you can use the following code:
```
PUT my_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "type": "custom",
          "tokenizer": "whitespace",
          "filter": [
            "lowercase"
          ]
        }
      }
    }
  }
}
```

The output of the above code is:
```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "my_index"
}
```

To use the analyzer, you can use the analyze API to test the analyzer:
```
GET my_index/_analyze
{
  "analyzer": "my_analyzer",
  "text": "This is a Test"
}
```

The output of the above code is:
```
{
  "tokens": [
    {
      "token": "this",
      "start_offset": 0,
      "end_offset": 4,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "is",
      "start_offset": 5,
      "end_offset": 7,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "a",
      "start_offset": 8,
      "end_offset": 9,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "test",
      "start_offset": 10,
      "end_offset": 14,
      "type": "<ALPHANUM>",
      "position": 3
    }
  ]
}
```

The above example shows how to use an Elasticsearch analyzer.

## Helpful links

- [Elasticsearch Analyzers](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-analyzers.html)
- [Analyze API](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-analyze.html)

onelinerhub: [How do I use an Elasticsearch analyzer?](https://onelinerhub.com/elasticsearch/how-do-i-use-an-elasticsearch-analyzer)