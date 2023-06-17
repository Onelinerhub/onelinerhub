# How can I use PostgreSQL XML functions to manipulate XML data?
// plain

PostgreSQL provides several functions for manipulating XML data. The following example code block demonstrates the use of the `xpath()` and `xmlelement()` functions to extract and modify data from an XML document:

```
SELECT xmlelement(name title, xpath('/book/title/text()', bookxml))
FROM booktable
WHERE bookid = 123;
```

This code will extract the title element from the bookxml column in the booktable table, where the bookid is 123. The output of this code will be the title of the book with the ID 123.

The `xmlexists()` function can be used to check if a certain node exists in an XML document. The following example code block demonstrates the use of the `xmlexists()` function to check if an author element exists in an XML document:

```
SELECT xmlexists('/book/author' PASSING BY bookxml)
FROM booktable
WHERE bookid = 123;
```

This code will return `true` if an author element exists in the bookxml column of the booktable table where the bookid is 123.

The `xmlforest()` function can be used to extract multiple elements from an XML document. The following example code block demonstrates the use of the `xmlforest()` function to extract multiple elements from an XML document:

```
SELECT xmlforest(title, author, publisher)
FROM booktable
WHERE bookid = 123;
```

This code will extract the title, author and publisher elements from the bookxml column in the booktable table, where the bookid is 123. The output of this code will be a row containing the title, author and publisher of the book with the ID 123.

## Helpful links
- https://www.postgresql.org/docs/current/functions-xml.html
- https://www.postgresql.org/docs/current/xpath.html

onelinerhub: [How can I use PostgreSQL XML functions to manipulate XML data?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-xml-functions-to-manipulate-xml-data)