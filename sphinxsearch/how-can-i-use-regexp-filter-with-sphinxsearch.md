# How can I use regexp_filter with Sphinxsearch?
// plain

The regexp_filter is a powerful tool that can be used with Sphinxsearch to filter search results based on a regular expression pattern. This tutorial will show you how to use regexp_filter with Sphinxsearch.

1. Create a Sphinx configuration file, and define an index with the regexp_filter option. For example:
```
source data_source
{
    type = mysql
    sql_query = \
        SELECT id, title, content \
        FROM table
    sql_attr_uint = id
    sql_attr_string = title
    sql_attr_string = content
    sql_field_string = title
    sql_field_string = content
    sql_query_info = SELECT * FROM table WHERE id=$id
    index title
    {
        type = plain
        regexp_filter = (\w+)
    }
    index content
    {
        type = plain
        regexp_filter = (\w+)
    }
}
```
2. Once the configuration file is created, run the indexer command to create the index:
```
indexer --config /path/to/sphinx.conf --all
```

3. After the index is created, you can now use the regexp_filter option in your search query. For example:
```
$query = 'SELECT * FROM data_source WHERE MATCH('title:myword regexp_filter:(\w+)')';
```
This will return all records that contain the word 'myword', as well as any words that match the regular expression pattern.

## Helpful links
- [Sphinxsearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Regular Expression Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How can I use regexp_filter with Sphinxsearch?](https://onelinerhub.com/sphinxsearch/how-can-i-use-regexp-filter-with-sphinxsearch)