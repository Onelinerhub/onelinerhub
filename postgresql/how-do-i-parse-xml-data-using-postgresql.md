# How do I parse XML data using PostgreSQL?
// plain

PostgreSQL can parse XML data using the `xml` data type and several functions and operators that are available to work with it.

To parse XML data, you need to first convert it into the `xml` data type. This can be done using the `xmlparse` function. For example:
```
SELECT xmlparse(document '<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>');
```

The output of this code will be:
```
   xmlparse
---------------
  <note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
  </note>
(1 row)
```

Once the XML data is in the `xml` data type, you can use the `xpath` function to extract values from the XML. For example:
```
SELECT xpath('/note/to/text()', xmlparse(document '<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>'));
```

The output of this code will be:
```
 xpath
-------
 Tove
(1 row)
```

You can also use the `xmlexists` function to check if a certain node exists in the XML. For example:
```
SELECT xmlexists('/note/from[text() = "Jani"]'
   PASSING BY VALUE xmlparse(document '<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>'));
```

The output of this code will be:
```
 xmlexists
-----------
 t
(1 row)
```

## Helpful links
- [PostgreSQL Documentation - XML Types](https://www.postgresql.org/docs/current/datatype-xml.html)
- [PostgreSQL Documentation - XPath Functions](https://www.postgresql.org/docs/current/xpath.html)

onelinerhub: [How do I parse XML data using PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-parse-xml-data-using-postgresql)