# How do I use a PostgreSQL XML parser in an example?
// plain

PostgreSQL provides an XML parser for parsing XML documents.

To use it in an example, you can use the `xmlelement` function to construct an XML document from a set of values. The following code block shows an example of how to use it:

```
SELECT xmlelement(name "root",
                  xmlelement(name "child1", 'value1'),
                  xmlelement(name "child2", 'value2'))

```

The output of the above code is an XML document with two child elements, `child1` and `child2`, with the values `value1` and `value2` respectively:

```
<root><child1>value1</child1><child2>value2</child2></root>
```

You can also use the `xpath` function to extract data from an XML document. For example, the following code block shows how to extract the value of the `child1` element:

```
SELECT xpath('/root/child1/text()',
             xmlelement(name "root",
                  xmlelement(name "child1", 'value1'),
                  xmlelement(name "child2", 'value2')))
```

The output of the above code is `value1`:

```
{value1}
```

For more information about PostgreSQL XML parser, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-xml.html).

onelinerhub: [How do I use a PostgreSQL XML parser in an example?](https://onelinerhub.com/postgresql/how-do-i-use-a-postgresql-xml-parser-in-an-example)