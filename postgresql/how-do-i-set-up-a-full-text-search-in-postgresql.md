# How do I set up a full text search in PostgreSQL?
// plain

Setting up a full text search in PostgreSQL is relatively straightforward.

First, create a table with the columns you need for your search, such as `title`, `body`, and `tags`.

```
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    body TEXT NOT NULL,
    tags VARCHAR[]
);
```

Next, create a GIN index on the `tags` column to enable searching.

```
CREATE INDEX documents_tags_idx ON documents USING GIN (tags);
```

Then, use the `to_tsvector` function to generate a searchable vector from the `title` and `body` columns.

```
SELECT to_tsvector('english', title || ' ' || body)
FROM documents;
```

Finally, use the `to_tsquery` function to generate a searchable query from the user's input.

```
SELECT to_tsquery('english', 'search phrase')
```

You can then use the `@@` operator to perform the full text search.

```
SELECT * FROM documents
WHERE to_tsvector('english', title || ' ' || body) @@ to_tsquery('english', 'search phrase');
```

## Helpful links

- [PostgreSQL Documentation - Full Text Search](https://www.postgresql.org/docs/current/textsearch.html)
- [PostgreSQL Documentation - to_tsvector](https://www.postgresql.org/docs/current/textsearch-controls.html#TEXTSEARCH-PARSING-DOCUMENTS)
- [PostgreSQL Documentation - to_tsquery](https://www.postgresql.org/docs/current/textsearch-controls.html#TEXTSEARCH-QUERIES)

onelinerhub: [How do I set up a full text search in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-set-up-a-full-text-search-in-postgresql)