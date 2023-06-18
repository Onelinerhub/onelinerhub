# How can I use SphinxSearch and Sngrl together to optimize search results?
// plain

SphinxSearch and Sngrl can be used together to optimize search results.

First, SphinxSearch should be used to create a full-text index of the data that needs to be searched. This index can then be used in conjunction with Sngrl to create a more powerful and accurate search query.

Example code for creating a full-text index using SphinxSearch:
```
index myindex
{
    type = rt
    path = /path/to/myindex
    rt_field = title
    rt_field = content
    rt_attr_uint = category
    rt_attr_timestamp = publish_date
}
```

This code will create a full-text index named "myindex" with the fields "title" and "content" as well as the attributes "category" and "publish_date".

Once the index is created, Sngrl can be used to create a more powerful search query. For example, the following query will search for documents with the words "cat" and "dog" in the title field and the category attribute equal to "2":

```
SELECT * FROM myindex
WHERE MATCH('@title cat @title dog')
AND @category = 2
```

Using SphinxSearch and Sngrl together can help to optimize search results by allowing more powerful search queries to be created.

## Code explanation
**
- **index myindex** - This creates an index named "myindex".
- **type = rt** - This sets the type of index to "rt" which stands for real-time index.
- **path = /path/to/myindex** - This sets the path for the index.
- **rt_field = title** - This sets the "title" field as a real-time field.
- **rt_field = content** - This sets the "content" field as a real-time field.
- **rt_attr_uint = category** - This sets the "category" attribute as an unsigned integer.
- **rt_attr_timestamp = publish_date** - This sets the "publish_date" attribute as a timestamp.
- **MATCH('@title cat @title dog')** - This creates a full-text search query for the words "cat" and "dog" in the "title" field.
- **@category = 2** - This sets the "category" attribute to "2".

**## Helpful links**
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Sngrl Documentation](https://sngrl.com/docs/index.html)

onelinerhub: [How can I use SphinxSearch and Sngrl together to optimize search results?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinxsearch-and-sngrl-together-to-optimize-search-results)