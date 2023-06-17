# How do I create a view in PostgreSQL?
// plain

To create a view in PostgreSQL, you need to use the `CREATE VIEW` statement. The syntax of creating a view is as follows:

```
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

The `view_name` is the name of the view to be created. The `column1`, `column2`, etc. are the columns to be selected from the `table_name`. The `WHERE` clause is optional and specifies the conditions that must be met for the records to be included in the view.

For example, to create a view named `sales_view` from the `sales` table:

```
CREATE VIEW sales_view AS
SELECT customer_name, product, quantity
FROM sales
WHERE quantity > 5;
```

This will create a view that contains the `customer_name`, `product`, and `quantity` columns from the `sales` table, but only for records where the `quantity` is greater than 5.

## Code explanation
**

1. `CREATE VIEW` - statement used to create a view
2. `view_name` - name of the view to be created
3. `column1`, `column2`, etc. - columns to be selected from the table
4. `table_name` - name of the table from which to select columns
5. `WHERE` clause - optional condition that must be met for records to be included in the view

**## Helpful links**

- [PostgreSQL Documentation - CREATE VIEW](https://www.postgresql.org/docs/current/sql-createview.html)

onelinerhub: [How do I create a view in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-create-a-view-in-postgresql)