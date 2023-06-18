# How do I configure SphinxSearch using YAML?
// plain

Configuring SphinxSearch using YAML is a simple process. The following example code block shows a basic configuration:

```
index:
  name: product_index
  type: sphinx
  source: product
  path: db/sphinx/product_index
```

This code block defines an index named `product_index` of type `sphinx` that will be sourced from the `product` table and stored in the `db/sphinx/product_index` directory.

The following list explains the parts of the code block:
- `index`: the root element of the configuration
- `name`: the name of the index
- `type`: the type of index (in this case, `sphinx`)
- `source`: the source table for the index
- `path`: the directory where the index will be stored

For more information about configuring SphinxSearch using YAML, see the [official documentation](https://sphinxsearch.com/docs/current.html#conf-yaml).

onelinerhub: [How do I configure SphinxSearch using YAML?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-sphinxsearch-using-yaml)