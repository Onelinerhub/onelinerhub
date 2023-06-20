# How can I use Google Big Query to process XML data?
// plain

Google Big Query can be used to process XML data using the `EXTRACT` function. This function extracts specific data from an XML document and returns it as a string. The syntax for the `EXTRACT` function is as follows:

```
EXTRACT(XML, xpath_expr)
```

where `XML` is the XML document and `xpath_expr` is an XPath expression that specifies the data to extract.

For example, if the XML document is as follows:

```
<root>
  <person>
    <name>John</name>
    <age>30</age>
  </person>
</root>
```

Then the following query can be used to extract the person's name:

```
SELECT EXTRACT(XML, '//person/name/text()')
```

The output of this query would be `John`.

## Code explanation


- `EXTRACT`: This is the Big Query function used to extract data from an XML document.
- `XML`: This is the XML document from which data will be extracted.
- `xpath_expr`: This is an XPath expression that specifies the data to extract.

## Helpful links

- [Google Big Query Documentation](https://cloud.google.com/bigquery/docs/)
- [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)

onelinerhub: [How can I use Google Big Query to process XML data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-to-process-xml-data)