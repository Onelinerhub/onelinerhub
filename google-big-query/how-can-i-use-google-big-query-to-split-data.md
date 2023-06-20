# How can I use Google Big Query to split data?
// plain

Google BigQuery allows you to split data into multiple tables using the `CREATE OR REPLACE TABLE` statement. The syntax is as follows:

```
CREATE OR REPLACE TABLE <destination_table>
AS
SELECT *
FROM <source_table>
WHERE <condition>
```

The `<destination_table>` is the name of the table that will be created with the data that satisfies the condition. The `<source_table>` is the name of the table from which the data will be taken. The `<condition>` is an expression that determines which rows of the source table will be included in the destination table.

For example, to split the table `users` into two tables `users_male` and `users_female` based on the gender field, the following query can be used:

```
CREATE OR REPLACE TABLE users_male
AS
SELECT *
FROM users
WHERE gender = 'male'

CREATE OR REPLACE TABLE users_female
AS
SELECT *
FROM users
WHERE gender = 'female'
```

This will create two new tables, `users_male` and `users_female`, with the data from the `users` table that satisfy the specified conditions.

## Code explanation
**
- `CREATE OR REPLACE TABLE`: statement to create a new table or replace an existing one
- `SELECT *`: statement to select all columns from the source table
- `FROM <source_table>`: statement to specify the source table
- `WHERE <condition>`: statement to specify the condition for the rows to be included in the table

**## Helpful links**
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [SELECT Statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language#select_statement)
- [CREATE OR REPLACE TABLE Statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_or_replace_table_statement)

onelinerhub: [How can I use Google Big Query to split data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-to-split-data)