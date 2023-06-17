# How can I get a value from a PostgreSQL XML column?
// plain

You can get a value from a PostgreSQL XML column using the `xpath()` function.

## Example code

```
SELECT xpath('/foo/bar/text()', xml_column)
FROM some_table;
```

## Output example

```
┌───────────────────────┐
│    xpath              │
├───────────────────────┤
│ {SomeValue}           │
└───────────────────────┘
```

The code above uses the `xpath()` function to get the value of the `bar` node inside the `foo` node of the `xml_column` column.

## Code explanation

- `xpath()` - a PostgreSQL function used to get a value from an XML column
- `/foo/bar/text()` - an XPath expression used to specify the target node
- `xml_column` - the XML column from which the value is retrieved

## Helpful links
- [PostgreSQL Documentation - XPath Functions](https://www.postgresql.org/docs/current/xpath.html)

onelinerhub: [How can I get a value from a PostgreSQL XML column?](https://onelinerhub.com/postgresql/how-can-i-get-a-value-from-a-postgresql-xml-column)