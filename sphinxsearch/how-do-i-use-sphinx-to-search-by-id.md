# How do I use Sphinx to search by ID?
// plain

Sphinx is a powerful open-source full-text search engine that can be used to search by ID. It is written in C++ and provides a fast and efficient way to search through large volumes of data.

To use Sphinx to search by ID, you will need to create an index for the ID field. To do this, you can use the following command:

```
index id_field
{
	type = rt
	rt_field = id
	rt_attr_uint = id
}
```

This command will create an index for the `id_field` with the type `rt` (real-time index). The `rt_field` parameter specifies the field in the data that contains the ID to be used for searching. The `rt_attr_uint` parameter specifies the data type of the ID field.

Once the index is created, you can use the following query to search by ID:

```
SELECT * FROM index_name WHERE MATCH('@id <id_value>')
```

This query will search the `index_name` index for documents with the specified `id_value`.

For more information on using Sphinx to search by ID, see the [Sphinx documentation](https://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I use Sphinx to search by ID?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinx-to-search-by-id)