# How do I decide whether to use PostgreSQL VARCHAR or TEXT data types?
// plain

When deciding whether to use PostgreSQL VARCHAR or TEXT data types, it is important to consider the size of the data that needs to be stored. VARCHAR is used to store strings with a maximum size of 65,535 bytes, while TEXT is used to store strings with a maximum size of 1GB.

The following example demonstrates the difference between the two data types:

```
CREATE TABLE string_table (
  id SERIAL PRIMARY KEY,
  string_varchar VARCHAR(255),
  string_text TEXT
);

INSERT INTO string_table (string_varchar, string_text)
VALUES ('This string is shorter than 255 characters', 'This string is longer than 255 characters and will be stored in the TEXT column');

SELECT * FROM string_table;
```
## Output example


| id | string_varchar                         | string_text                                                                                                                            |
|----|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 1  | This string is shorter than 255 characters | This string is longer than 255 characters and will be stored in the TEXT column                                                       |

If the data to be stored is larger than 65,535 bytes, then TEXT should be used. If the data is smaller than 65,535 bytes, then VARCHAR should be used. VARCHAR is generally more efficient than TEXT as it requires less memory to store the data.

## Helpful links
- [PostgreSQL Documentation: Character Types](https://www.postgresql.org/docs/current/datatype-character.html)
- [PostgreSQL Documentation: Insert](https://www.postgresql.org/docs/current/sql-insert.html)

onelinerhub: [How do I decide whether to use PostgreSQL VARCHAR or TEXT data types?](https://onelinerhub.com/postgresql/how-do-i-decide-whether-to-use-postgresql-varchar-or-text-data-types)