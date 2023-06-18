# How can I adjust the index field lengths when using Sphinx search?
// plain

The index field lengths in Sphinx can be adjusted using the `sql_field_string` directive. This directive allows you to specify the maximum length of string fields, which can be set to any value between 1 and 2^32-1.

For example, if you wanted to set the maximum length of a field to 255 characters, you could add the following directive to your Sphinx configuration file:

```
sql_field_string = myfield:255
```

The `sql_field_string` directive has the following parts:

- `sql_field_string`: This is the directive that tells Sphinx that you want to adjust the field length.
- `myfield`: This is the name of the field that you want to adjust.
- `255`: This is the maximum length of the field that you want to set.

## Helpful links

- [Sphinx Documentation - sql_field_string Directive](http://sphinxsearch.com/docs/current.html#conf-sql-field-string)

onelinerhub: [How can I adjust the index field lengths when using Sphinx search?](https://onelinerhub.com/sphinxsearch/how-can-i-adjust-the-index-field-lengths-when-using-sphinx-search)