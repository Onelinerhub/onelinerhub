# How do I use SphinxSearch with XMLPipe2?
// plain

SphinxSearch is a full-text search engine that can be used to store and query documents in a variety of formats. XMLPipe2 is a data source handler for SphinxSearch that allows you to index and query XML documents. To use XMLPipe2 with SphinxSearch, you need to create an XML document and then pass it to SphinxSearch using the `xmlpipe2` directive.

## Example code

```
index test_index
{
  type = xmlpipe2
  xmlpipe_command = cat /path/to/data.xml
}
```

This code will create an index called `test_index` and configure it to use the XMLPipe2 data source handler. The `xmlpipe_command` directive specifies the command to execute in order to generate the XML document. In this example, the command `cat /path/to/data.xml` is used to read the contents of the file `data.xml` and output the contents as XML.

Once the index is configured, you can query it using the SphinxSearch query language. For example, the following query will search for documents containing the word "example":

```
SELECT * FROM test_index WHERE MATCH('example');
```

The output of this query will be a list of documents containing the word "example".

## Code explanation

1. `index test_index` - Creates an index called `test_index`.
2. `type = xmlpipe2` - Configures the index to use the XMLPipe2 data source handler.
3. `xmlpipe_command = cat /path/to/data.xml` - Specifies the command to execute in order to generate the XML document.
4. `SELECT * FROM test_index WHERE MATCH('example');` - Searches for documents containing the word "example".

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/)
- [XMLPipe2 Documentation](http://sphinxsearch.com/docs/current.html#xmlpipe2)

onelinerhub: [How do I use SphinxSearch with XMLPipe2?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-with-xmlpipe-)