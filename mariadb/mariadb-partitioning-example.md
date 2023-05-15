# Mariadb partitioning example
// plain

Partitioning in MariaDB is a way to divide a large table into smaller, more manageable parts. It can improve query performance and reduce storage space.

## Example


```
CREATE TABLE sales (
  id INT NOT NULL,
  sale_date DATE NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
)
PARTITION BY RANGE (sale_date) (
  PARTITION p0 VALUES LESS THAN ('2020-01-01'),
  PARTITION p1 VALUES LESS THAN ('2020-02-01'),
  PARTITION p2 VALUES LESS THAN ('2020-03-01'),
  PARTITION p3 VALUES LESS THAN ('2020-04-01'),
  PARTITION p4 VALUES LESS THAN ('2020-05-01'),
  PARTITION p5 VALUES LESS THAN (MAXVALUE)
);
```

This example creates a table called `sales` with a `sale_date` column. The table is partitioned by range, with each partition containing data for a single month.

## Code explanation


- `CREATE TABLE sales`: creates a table called `sales`
- `PARTITION BY RANGE (sale_date)`: partitions the table by range, using the `sale_date` column
- `PARTITION p0 VALUES LESS THAN ('2020-01-01')`: creates a partition for data with a `sale_date` before 2020-01-01
- `PARTITION p5 VALUES LESS THAN (MAXVALUE)`: creates a partition for data with a `sale_date` after all other partitions

## Helpful links

- [MariaDB Documentation - Partitioning](https://mariadb.com/kb/en/library/partitioning/)

onelinerhub: [Mariadb partitioning example](https://onelinerhub.com/mariadb/mariadb-partitioning-example)