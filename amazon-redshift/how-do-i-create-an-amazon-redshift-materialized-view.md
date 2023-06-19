# How do I create an Amazon Redshift materialized view?
// plain

Creating a materialized view in Amazon Redshift requires the following steps:

1. Create a view using the `CREATE VIEW` command. This command defines the query that will be used to populate the materialized view. For example:
```
CREATE VIEW my_view AS
SELECT a, b, c
FROM table1
```

2. Create the materialized view using the `CREATE MATERIALIZED VIEW` command. This command defines the physical storage for the materialized view and the refresh interval. For example:
```
CREATE MATERIALIZED VIEW my_mview
FROM my_view
REFRESH EVERY 1 DAY
```

3. Refresh the materialized view using the `REFRESH MATERIALIZED VIEW` command. This command will populate the materialized view with the data from the view. For example:
```
REFRESH MATERIALIZED VIEW my_mview
```

4. To verify the materialized view was created successfully, use the `SELECT` command to query the materialized view. For example:
```
SELECT * FROM my_mview
```

For more information on creating and managing materialized views in Amazon Redshift, see the [Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_MATERIALIZED_VIEW.html).

onelinerhub: [How do I create an Amazon Redshift materialized view?](https://onelinerhub.com/amazon-redshift/how-do-i-create-an-amazon-redshift-materialized-view)