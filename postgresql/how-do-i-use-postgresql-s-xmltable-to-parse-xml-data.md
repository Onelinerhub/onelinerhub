# How do I use PostgreSQL's XMLTABLE to parse XML data?
// plain

XMLTABLE is a PostgreSQL function that allows you to parse XML data into SQL tables. It takes two arguments, an XML document and an XPath expression. The XPath expression is used to identify the elements in the XML document that should be used to generate the columns in the table.

## Example

```
WITH xmldata AS (
  SELECT '<book>
  <title>The Odyssey</title>
  <author>Homer</author>
  <publisher>Penguin Classics</publisher>
</book>'::xml AS xml_data
)
SELECT * FROM xmldata, XMLTABLE('/book' PASSING xml_data COLUMNS
  title TEXT PATH 'title',
  author TEXT PATH 'author',
  publisher TEXT PATH 'publisher'
);
```
## Output example

```
title        | author | publisher
-------------|--------|-----------
The Odyssey   | Homer  | Penguin Classics
```

## Code explanation

- `WITH xmldata AS (SELECT '<book>...</book>'::xml AS xml_data)`: This creates a temporary table containing the XML document we want to parse.
- `SELECT * FROM xmldata, XMLTABLE('/book' PASSING xml_data`: This is the XMLTABLE function. It takes two arguments, an XPath expression (in this case `/book`) and the XML document (in this case `xml_data`).
- `COLUMNS title TEXT PATH 'title', author TEXT PATH 'author', publisher TEXT PATH 'publisher'`: This specifies the columns to be generated from the XML document. The name of the column is specified first (`title`, `author`, `publisher`), followed by the type of data (`TEXT`) and the XPath expression to the element in the XML document that should be used to generate the column (`PATH 'title'`, `PATH 'author'`, `PATH 'publisher'`).

## Helpful links
- [PostgreSQL Documentation: XMLTABLE](https://www.postgresql.org/docs/current/xmltable.html)
- [Stack Overflow: How to use XMLTABLE in PostgreSQL?](https://stackoverflow.com/questions/55219092/how-to-use-xmltable-in-postgresql)

onelinerhub: [How do I use PostgreSQL's XMLTABLE to parse XML data?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-xmltable-to-parse-xml-data)