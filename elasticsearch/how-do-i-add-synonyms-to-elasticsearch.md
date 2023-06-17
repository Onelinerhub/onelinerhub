# How do I add synonyms to Elasticsearch?
// plain

Adding synonyms to Elasticsearch is a great way to improve the accuracy of your search results. Synonyms are words or phrases that have the same meaning as another word or phrase.

To add synonyms to Elasticsearch, you need to use the [`synonym_graph` token filter](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-synonym-tokenfilter.html). To do this, you must create an index with a settings and mapping file.

For example, the following settings and mapping file will create an index with the `synonym_graph` token filter:

```
PUT /my_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_synonyms": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "my_synonym_filter"
          ]
        }
      },
      "filter": {
        "my_synonym_filter": {
          "type": "synonym_graph",
          "synonyms": [
            "quick,fast",
            "slow,sluggish"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "text": {
        "type": "text",
        "analyzer": "my_synonyms"
      }
    }
  }
}
```

The `synonyms` array is where you can specify the synonyms you want to add. In this example, we have specified two sets of synonyms: `quick` and `fast`, and `slow` and `sluggish`.

Once you have created the index, you can use the `synonym_graph` token filter to analyze text and add the synonyms you have specified. For example:

```
POST /my_index/_analyze
{
  "analyzer": "my_synonyms",
  "text": "I'm looking for something quick"
}
```

This will return the following output:

```
{
  "tokens": [
    {
      "token": "i'm",
      "start_offset": 0,
      "end_offset": 3,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "looking",
      "start_offset": 4,
      "end_offset": 11,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "for",
      "start_offset": 12,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "something",
      "start_offset": 16,
      "end_offset": 25,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "quick",
      "start_offset": 26,
      "end_offset": 31,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "fast",
      "start_offset": 26,
      "end_offset": 31,
      "type": "SYNONYM",
      "position": 4
    }
  ]
}
```

As you can see, the `synonym_graph` token filter has added the synonym `fast` to the text.

## Code explanation
**

1. `PUT /my_index` - Creates the index with settings and mapping file
2. `"tokenizer": "standard"` - Specifies the tokenizer to use
3. `"filter": [ "lowercase", "my_synonym_filter" ]` - Specifies the filter to use
4. `"type": "synonym_graph"` - Specifies the type of token filter to use
5. `"synonyms": [ "quick,fast", "slow,sluggish" ]` - Specifies the synonyms to add
6. `POST /my_index/_analyze` - Analyzes the text and adds the synonyms

**## Helpful links**

- [Elasticsearch Synonym Token Filter Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-synonym-tokenfilter.html)

onelinerhub: [How do I add synonyms to Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-add-synonyms-to-elasticsearch)