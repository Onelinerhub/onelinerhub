# How to work with XML in Mariadb?
// plain

Mariadb supports the use of XML data type and functions to work with XML documents.

The following example shows how to create a table with an XML column and insert a document into it:

```
CREATE TABLE xml_table (
  id INT NOT NULL AUTO_INCREMENT,
  xml_doc XML,
  PRIMARY KEY (id)
);

INSERT INTO xml_table (xml_doc) VALUES
  ('<root><name>John Doe</name><age>30</age></root>');
```

The output of the above code will be:

```
Query OK, 1 row affected (0.01 sec)
```

To extract data from the XML document, the following functions can be used:

- `EXTRACTVALUE()`: Extracts a value from an XML document.
- `UPDATEXML()`: Updates an XML document.
- `DELETEXML()`: Deletes an XML document.

## Helpful links

- [Mariadb XML Functions](https://mariadb.com/kb/en/library/xml-functions/)
- [Mariadb XML Data Type](https://mariadb.com/kb/en/library/xml-data-type/)

onelinerhub: [How to work with XML in Mariadb?](https://onelinerhub.com/mariadb/how-to-work-with-xml-in-mariadb)