# How do I insert data into Google BigQuery?
// plain

You can insert data into Google BigQuery using the `INSERT` statement. For example, the following code block inserts a row into a table called `mydataset.mytable`:

```
INSERT INTO mydataset.mytable (col1, col2, col3)
VALUES (1, 'a', 'hello');
```

This statement will insert a row with values of 1, 'a', and 'hello' into the three columns `col1`, `col2`, and `col3` of the table `mydataset.mytable`.

You can also use the `LOAD` statement to load data from a file. For example, the following code block loads data from a CSV file:

```
LOAD DATA INFILE 'mydata.csv'
INTO TABLE mydataset.mytable
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

This statement will load the data from the file `mydata.csv` into the table `mydataset.mytable`. The `FIELDS TERMINATED BY`, `ENCLOSED BY`, and `LINES TERMINATED BY` parameters specify the file format, and the `IGNORE 1 ROWS` parameter tells BigQuery to skip the first row of the file.

You can also use the `INSERT` statement to insert data from a query. For example, the following statement inserts the results of a query into the table `mydataset.mytable`:

```
INSERT INTO mydataset.mytable (col1, col2, col3)
SELECT colA, colB, colC
FROM otherdataset.othertable;
```

This statement will insert the results of the query into the table `mydataset.mytable`.

You can find more information about inserting data into BigQuery in the [BigQuery documentation](https://cloud.google.com/bigquery/docs/loading-data).

onelinerhub: [How do I insert data into Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-insert-data-into-google-bigquery)