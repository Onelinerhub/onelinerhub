# How do I add a column to an Amazon Redshift table?
// plain

Adding a column to an Amazon Redshift table can be done with the ALTER TABLE command. The following example code adds a new column to a table called `users`:

```
ALTER TABLE users
ADD COLUMN user_name VARCHAR(50);
```

This code adds a new column called `user_name` with a data type of VARCHAR(50) to the `users` table. After running the command, the `users` table will have an additional column.

## Code explanation


1. `ALTER TABLE` - Used to change the structure of an existing table.
2. `users` - The name of the table to add a column to.
3. `ADD COLUMN` - Used to add a new column to a table.
4. `user_name` - The name of the new column to add.
5. `VARCHAR(50)` - The data type of the new column.

Here are some relevant links about adding columns to Amazon Redshift tables:

- [Altering Tables](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_TABLE.html)
- [Data Types](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html)

onelinerhub: [How do I add a column to an Amazon Redshift table?](https://onelinerhub.com/amazon-redshift/how-do-i-add-a-column-to-an-amazon-redshift-table)