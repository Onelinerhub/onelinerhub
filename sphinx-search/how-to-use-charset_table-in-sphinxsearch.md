# How to use charset_table in SphinxSearch?
// plain

SphinxSearch supports a charset_table option to define a custom character set for indexing and searching. This option is used to define a mapping between characters in the source text and characters in the index.

## Example

```
index test
{
    charset_table = 0..9, A..Z->a..z, _, a..z, U+410..U+42F->U+430..U+44F, U+430..U+44F
}
```

This example defines a mapping between characters 0-9, A-Z to a-z, _, a-z, and Cyrillic characters U+410-U+42F to U+430-U+44F.

## Code explanation

- `index test`: defines the index name
- `charset_table`: defines the character set mapping
- `0..9`: defines the range of characters 0-9
- `A..Z->a..z`: defines the mapping of characters A-Z to a-z
- `_`: defines the character _
- `a..z`: defines the range of characters a-z
- `U+410..U+42F->U+430..U+44F`: defines the mapping of Cyrillic characters U+410-U+42F to U+430-U+44F

## Helpful links
- [SphinxSearch Documentation - charset_table](http://sphinxsearch.com/docs/current.html#conf-charset-table)

onelinerhub: [How to use charset_table in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-charset_table-in-sphinxsearch)