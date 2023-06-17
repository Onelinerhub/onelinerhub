# How do I use the match_phrase query in Elasticsearch?
// plain

The `match_phrase` query in Elasticsearch is used to search for exact phrases in fields. It is especially useful when you need to find a phrase that is composed of multiple words.

For example, the following query searches for documents that contain the exact phrase "quick brown fox":
```
GET /_search
{
  "query": {
    "match_phrase": {
      "text": "quick brown fox"
    }
  }
}
```
The output of this query would be documents that contain the exact phrase "quick brown fox".

The `match_phrase` query has several components:
- The `match_phrase` keyword, which tells Elasticsearch to use the `match_phrase` query.
- The field to search in, which is specified by the `text` field in this example.
- The phrase to search for, which is specified by the `"quick brown fox"` string in this example.

For more information, please see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query-phrase.html).

onelinerhub: [How do I use the match_phrase query in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-use-the-match-phrase-query-in-elasticsearch)