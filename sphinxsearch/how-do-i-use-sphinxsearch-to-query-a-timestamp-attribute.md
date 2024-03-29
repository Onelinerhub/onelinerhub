# How do I use SphinxSearch to query a timestamp attribute?
// plain

SphinxSearch is an open source search engine that can be used to query a timestamp attribute. To use SphinxSearch to query a timestamp attribute, you must first create a Sphinx configuration file. In the configuration file, you must define the index, specify the data source, and set the timestamp attribute field.

For example, the following configuration file defines an index called `timestamp_index`, uses a MySQL data source, and sets the timestamp attribute field to `date_created`:
```
index timestamp_index
{
    type = plain
    source = timestamp_source
    path = /var/data/timestamp_index
    docinfo = extern
    mlock = 0
    min_word_len = 1
    charset_type = utf-8
    charset_table = 0..9, A..Z->a..z, _, a..z, U+80..U+FF->U+0080..U+00FF, U+1000..U+FFFF
    html_strip = 0
    html_index_attrs =
    html_remove_elements =
    min_prefix_len = 0
    min_infix_len = 0
    expand_keywords = 1
    dict = keywords
    stopwords =
    enable_star = 1
    min_stemming_len = 1
    ignore_chars = U+002D
    index_exact_words = 1
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones =
    index_field_lengths = 1
    index_sp = 0
    index_zones

onelinerhub: [How do I use SphinxSearch to query a timestamp attribute?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-to-query-a-timestamp-attribute)