# How do I use SphinxSearch to create a snippet?
// plain

SphinxSearch is a powerful open-source full-text search engine. It can be used to create snippets, which are short pieces of text that provide an overview of a document or webpage.

To create a snippet with SphinxSearch, first create an index of the documents or webpages that you want to search. This can be done with the `indexer` command. For example:

```
indexer --config config.conf --all
```

This will create an index of all documents or webpages specified in `config.conf`.

Next, use the `search` command to search your index and retrieve the snippets for each result. For example:

```
search --config config.conf --snippets "query"
```

This command will search your index for the query “query” and return the snippets for each result.

You can customize the snippets by specifying the `--limit` and `--around` options. The `--limit` option specifies the maximum number of words in the snippet, while the `--around` option specifies the number of words to include before and after the matching words in the snippet.

For more information, see the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I use SphinxSearch to create a snippet?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-to-create-a-snippet)