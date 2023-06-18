# How do I use SphinxSearch DocInfo?
// plain

SphinxSearch DocInfo is a feature of the SphinxSearch full text search engine which allows you to store additional information about each document that you index. This can be used to improve the relevance of search results.

Here is an example of how to use SphinxSearch DocInfo:

```
index test
{
    docinfo = extern
    path = /var/data/test
}

index test_docinfo
{
    source = test
    type = docinfo
}
```

This will create two indexes, `test` and `test_docinfo`, which will store the document content and the DocInfo data respectively.

The `docinfo = extern` line in the `test` index tells Sphinx to store the DocInfo data in an external index, which in this case is `test_docinfo`.

When you query the `test` index, the results will include the DocInfo data from the `test_docinfo` index.

For more information on using SphinxSearch DocInfo, see the [SphinxSearch Documentation](https://sphinxsearch.com/docs/).

onelinerhub: [How do I use SphinxSearch DocInfo?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-docinfo)