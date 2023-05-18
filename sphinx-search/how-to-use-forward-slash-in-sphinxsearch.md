# How to use forward slash in SphinxSearch?
// plain

SphinxSearch uses forward slash (`/`) as a special character to separate search terms. It is used to search for exact phrases, and to group search terms together.

## Example

```
SELECT * FROM documents WHERE MATCH('"hello world"/2');
```
This query will search for documents containing the exact phrase "hello world" with a maximum of two words between them.

## Code explanation


- `SELECT * FROM documents`: This part of the code selects all columns from the documents table.
- `WHERE MATCH('"hello world"/2')`: This part of the code searches for documents containing the exact phrase "hello world" with a maximum of two words between them.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How to use forward slash in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-forward-slash-in-sphinxsearch)