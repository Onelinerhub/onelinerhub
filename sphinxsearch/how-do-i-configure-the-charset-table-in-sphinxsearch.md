# How do I configure the charset_table in SphinxSearch?
// plain

The charset_table configuration option in SphinxSearch allows you to specify the character set table used for full-text indexing. It is a comma-separated list of words, each word being a character or a range of characters.

For example, to set the charset_table to include all English letters, numbers, and some punctuation, you could use the following configuration:

```
charset_table = 0..9, A..Z->a..z, _, -, \
```

The above example would include all numbers (0-9), all English letters (both upper and lower case), underscore (_), hyphen (-), and backslash (\).

The following is a more detailed breakdown of the characters included in the example configuration above:

- 0..9 – all numbers from 0 to 9
- A..Z->a..z – all English letters from A to Z, as well as their lowercase counterparts from a to z
- _ – underscore
- - – hyphen
- \ – backslash

For more information about configuring the charset_table, please refer to the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html#conf-charset-table).

onelinerhub: [How do I configure the charset_table in SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-the-charset-table-in-sphinxsearch)