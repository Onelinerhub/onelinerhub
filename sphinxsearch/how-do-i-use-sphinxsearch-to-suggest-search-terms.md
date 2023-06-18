# How do I use SphinxSearch to suggest search terms?
// plain

SphinxSearch is an open source full-text search engine that can be used to suggest search terms. To use SphinxSearch to suggest search terms, you first need to create an index with the fields you want to search and suggest. You can then use the `SphinxQL` query language to query the index and suggest terms.

For example, you can create a `sphinx.conf` file with the following contents:

```
source src1
{
    type            = mysql
    sql_host        = localhost
    sql_user        = root
    sql_pass        =
    sql_db          = test
    sql_query_pre   = SET NAMES utf8
    sql_query       = SELECT id, title FROM documents
}

index test1
{
    source          = src1
    path            = /var/lib/sphinx/test1
    docinfo         = extern
    mlock           = 0
    morphology      = stem_en
    min_word_len    = 2
    charset_type    = utf-8
    charset_table   = 0..9, A..Z->a..z, _, a..z, U+410..U+42F->U+430..U+44F, U+430..U+44F
}
```

Then you can use the following `SphinxQL` query to suggest terms:

```
SELECT * FROM test1 WHERE MATCH('@title *') OPTION ranker=expr('sum(lcs*user_weight)*1000+bm25');
```

This query will return all documents that match the search term, as well as a score for each document. The documents with the highest scores are the most relevant documents and can be used to suggest search terms.

* `source`: This section defines the source of the data that will be indexed.
* `index`: This section defines the index name and the settings for that index.
* `sql_query`: This is the SQL query used to retrieve data from the source.
* `MATCH`: This is the SphinxQL query used to search the index and suggest terms.
* `OPTION ranker`: This is the ranking algorithm used to score the documents.

## Helpful links
* [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
* [SphinxQL Syntax](http://sphinxsearch.com/docs/current.html#sphinxql-syntax)

onelinerhub: [How do I use SphinxSearch to suggest search terms?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-to-suggest-search-terms)