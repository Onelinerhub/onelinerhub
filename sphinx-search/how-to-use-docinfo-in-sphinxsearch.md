# How to use docinfo in SphinxSearch?
// plain

Docinfo is a feature of SphinxSearch that allows you to store additional information about documents in the index. This information can be used to improve search performance and to provide additional information about documents in search results.

## Example code

```
index test
{
    docinfo = extern
    path = /var/data/test
}
```

This code will create an index called "test" and enable the docinfo feature. The path parameter specifies the location of the external docinfo file.

## Code explanation

- index: specifies the name of the index
- docinfo: enables the docinfo feature
- path: specifies the location of the external docinfo file

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Docinfo Feature](http://sphinxsearch.com/docs/current.html#conf-docinfo)

onelinerhub: [How to use docinfo in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-docinfo-in-sphinxsearch)