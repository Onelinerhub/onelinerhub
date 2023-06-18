# How do I use the sphinxsearch sql_attr_multi attribute?
// plain

The `sql_attr_multi` attribute is used to create multi-value attributes in Sphinx. It allows the user to index multiple values for a single document, which can then be used for filtering.

For example, if you wanted to index multiple tags for a blog post, you could use the `sql_attr_multi` attribute.

```
sql_attr_multi = uint tags from query;
SELECT post_id, GROUP_CONCAT(tag_id) as tags FROM post_tags GROUP BY post_id
```

This query will return a list of post IDs and associated tag IDs, which can then be used to set up the `sql_attr_multi` attribute.

The `sql_attr_multi` attribute has three parts:
1. `uint`: The data type of the attribute.
2. `tags`: The name of the attribute.
3. `from query`: The query used to generate the multi-value attribute.

The output of the above query will look something like this:

```
post_id  tags
1        1,4,7
2        2,5,8
3        3,6,9
```

Using the `sql_attr_multi` attribute, you can then filter documents based on the tags associated with them.

## Helpful links
- [Sphinx Documentation - sql_attr_multi](http://sphinxsearch.com/docs/current.html#conf-sql-attr-multi)

onelinerhub: [How do I use the sphinxsearch sql_attr_multi attribute?](https://onelinerhub.com/sphinxsearch/how-do-i-use-the-sphinxsearch-sql-attr-multi-attribute)