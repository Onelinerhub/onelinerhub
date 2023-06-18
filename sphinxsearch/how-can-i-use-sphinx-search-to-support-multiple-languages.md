# How can I use Sphinx search to support multiple languages?
// plain

Sphinx search can be used to support multiple languages by using its built-in morphology and stemming capabilities. It can be used to index words from different languages, and then search for them using the same query.

For example, if we have a table with a text field containing words from French and English, we can use the following code to create an index:

```
index test
{
    source = test_source
    path = /var/lib/sphinxsearch/data/test
    morphology = stem_enru
    min_word_len = 3
}
```

This will create an index that supports both English and French words.

To use the index to search for words from different languages, we can use the following query:

```
SELECT * FROM test WHERE MATCH('@text (english | french)');
```

This will search the `text` field for words from both English and French.

The following list explains the parts of the code:

- `index test`: This creates the index with the name `test`.
- `source = test_source`: This specifies the source of the data that will be indexed.
- `path = /var/lib/sphinxsearch/data/test`: This specifies the path to the directory where the index will be stored.
- `morphology = stem_enru`: This specifies the morphology to be used for the index. In this case, it is set to `stem_enru`, which supports English and French.
- `min_word_len = 3`: This sets the minimum length of words that will be indexed.
- `SELECT * FROM test WHERE MATCH('@text (english | french)')`: This query searches the `text` field for words from both English and French.

## Helpful links

- [Sphinx Documentation](http://sphinxsearch.com/docs/)
- [Sphinx Morphology](http://sphinxsearch.com/docs/current.html#conf-morphology)

onelinerhub: [How can I use Sphinx search to support multiple languages?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinx-search-to-support-multiple-languages)