# How can I implement full text search in SQLite?
// plain

Full text search in SQLite can be implemented using the FTS3 and FTS4 extensions. FTS3 and FTS4 are virtual table modules that allow users to perform full-text searches on a set of documents. FTS3 is an older version of FTS4, but both provide similar functionality.

## Example code

```
CREATE VIRTUAL TABLE documents USING fts4 (content TEXT);

INSERT INTO documents VALUES ('This is an example document.');

SELECT * FROM documents WHERE documents MATCH 'example';
```
## Output example

```
This is an example document.
```

The example code creates a virtual table using the FTS4 module, inserts a document into the table, and then performs a full-text search on the table using the MATCH operator. This example returns the document that contains the word "example".

The FTS4 module provides several useful features for full-text search, including the ability to specify the language of the documents, the ability to perform phrase searches, and the ability to perform fuzzy searches.

## Helpful links
- [SQLite FTS3 and FTS4 Extensions](https://www.sqlite.org/fts3.html)
- [SQLite FTS3 and FTS4 Documentation](https://www.sqlite.org/fts3.html#section_2)
- [SQLite Full Text Search Tutorial](https://www.sqlitetutorial.net/sqlite-full-text-search/)

onelinerhub: [How can I implement full text search in SQLite?](https://onelinerhub.com/sqlite/how-can-i-implement-full-text-search-in-sqlite)