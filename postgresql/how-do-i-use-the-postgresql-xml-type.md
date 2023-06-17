# How do I use the PostgreSQL XML type?
// plain

PostgreSQL XML type is used to store XML data in a PostgreSQL database. It is a special data type that can store XML documents and fragments in a structured way.

To use the PostgreSQL XML type, you must first define a table with the XML type column. For example:

```
CREATE TABLE myTable (
    id SERIAL PRIMARY KEY,
    xml_data XML
);
```

This creates a table named `myTable` with an `id` column of type `SERIAL` and a `xml_data` column of type `XML`.

Then, you can insert data into the table using the `INSERT` statement. For example:

```
INSERT INTO myTable (xml_data)
VALUES ('<some_xml> <data>value1</data> <data>value2</data> </some_xml>');
```

Once the data is inserted, you can query the table and retrieve the XML data using the `SELECT` statement. For example:

```
SELECT xml_data FROM myTable;
```

This will return the XML data stored in the `xml_data` column.

You can also use XPath to query the XML data. For example:

```
SELECT xml_data->'data' FROM myTable;
```

This will return the value of the `data` element from the XML data.

## Helpful links
- [PostgreSQL Documentation - XML Type](https://www.postgresql.org/docs/9.4/datatype-xml.html)
- [PostgreSQL Documentation - XPath](https://www.postgresql.org/docs/9.4/xpath.html)

onelinerhub: [How do I use the PostgreSQL XML type?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-xml-type)