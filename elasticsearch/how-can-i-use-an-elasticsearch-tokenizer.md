# How can I use an Elasticsearch tokenizer?
// plain

An Elasticsearch tokenizer is a tool used to break down a string or text into individual tokens. These tokens can then be used for various purposes, such as indexing, searching, or analysis.

For example, the following code uses the standard tokenizer to break a string into tokens:

```
PUT my_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "standard"
        }
      }
    }
  }
}

POST my_index/_analyze
{
  "analyzer": "my_analyzer",
  "text": "This is a sample sentence"
}
```

The output of the above code is as follows:

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
      "token": "sample",
      "start_offset": 10,
      "end_offset": 16,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "sentence",
      "start_offset": 17,
      "end_offset": 25,
      "type": "<ALPHANUM>",
      "position": 4
    }
  ]
}
```

In the above example, the standard tokenizer takes the string "This is a sample sentence" and splits it into individual tokens: "this", "is", "a", "sample", and "sentence". Each token is then assigned a start and end offset, a type, and a position.

In addition to the standard tokenizer, Elasticsearch also offers a wide range of other tokenizers, such as the edge n-gram tokenizer, the keyword tokenizer, and the whitespace tokenizer.

For more information on using tokenizers in Elasticsearch, refer to the following links:

- [Elasticsearch Tokenizers](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenizers.html)
- [Elasticsearch Analyzers](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-analyzers.html)

onelinerhub: [How can I use an Elasticsearch tokenizer?](https://onelinerhub.com/elasticsearch/how-can-i-use-an-elasticsearch-tokenizer)