# How do I configure SphinxSearch to use morphology?
// plain

In order to configure SphinxSearch to use morphology, you must first enable the morphology feature in the `sphinx.conf` configuration file. To do so, add the following line to the configuration file:

```
morphology = stem_en, soundex
```

This will enable the stem_en and soundex morphological processors, which will allow SphinxSearch to perform morphological analysis on text.

You must also specify a dictionary file for the morphological processor. To do so, add the following line to the configuration file:

```
morphology_dict = /path/to/dictionary.dict
```

This will enable the morphology processor to use the dictionary file located at `/path/to/dictionary.dict`.

Finally, you must specify the indexing mode for the morphological processor. To do so, add the following line to the configuration file:

```
morphology_index = stem_en
```

This will enable the stem_en morphological processor to be used for indexing.

Once these settings have been configured, SphinxSearch will be configured to use morphology.

## Code explanation
**

1. `morphology = stem_en, soundex` - This line enables the stem_en and soundex morphological processors, which will allow SphinxSearch to perform morphological analysis on text.

2. `morphology_dict = /path/to/dictionary.dict` - This line specifies the dictionary file for the morphological processor.

3. `morphology_index = stem_en` - This line specifies the indexing mode for the morphological processor.

**## Helpful links**

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Morphology in SphinxSearch](http://sphinxsearch.com/docs/current.html#conf-morphology)

onelinerhub: [How do I configure SphinxSearch to use morphology?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-sphinxsearch-to-use-morphology)