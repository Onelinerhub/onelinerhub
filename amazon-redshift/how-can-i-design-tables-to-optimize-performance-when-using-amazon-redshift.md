# How can I design tables to optimize performance when using Amazon Redshift?
// plain

When designing tables to optimize performance when using Amazon Redshift, there are several best practices to consider.

1. Use Columnar Storage: Columnar storage is designed to speed up queries that involve only a few columns of a large table. To enable columnar storage, use the `CREATE TABLE` command with the `WITH (columnstore=on)` option.

```
CREATE TABLE sales
(
   sales_id INTEGER NOT NULL,
   product_id INTEGER NOT NULL,
   store_id INTEGER NOT NULL,
   quantity INTEGER NOT NULL
)
WITH (columnstore=on);
```

2. Use Sort Keys: Sort keys are used to physically order the data in a table. To enable sort keys, use the `CREATE TABLE` command with the `DISTKEY` and `SORTKEY` options.

```
CREATE TABLE sales
(
   sales_id INTEGER NOT NULL,
   product_id INTEGER NOT NULL,
   store_id INTEGER NOT NULL,
   quantity INTEGER NOT NULL
)
DISTKEY(store_id)
SORTKEY(product_id);
```

3. Use Compression: Compression is used to reduce the size of a table, which can improve performance. To enable compression, use the `CREATE TABLE` command with the `DISTSTYLE` and `COMPTYPE` options.

```
CREATE TABLE sales
(
   sales_id INTEGER NOT NULL,
   product_id INTEGER NOT NULL,
   store_id INTEGER NOT NULL,
   quantity INTEGER NOT NULL
)
DISTSTYLE KEY
COMPTYPE ZSTD;
```

4. Use Distribution Styles: Distribution styles determine how data is distributed across nodes. To enable distribution styles, use the `CREATE TABLE` command with the `DISTSTYLE` option.

```
CREATE TABLE sales
(
   sales_id INTEGER NOT NULL,
   product_id INTEGER NOT NULL,
   store_id INTEGER NOT NULL,
   quantity INTEGER NOT NULL
)
DISTSTYLE ALL;
```

By following these best practices when designing tables, you can optimize performance when using Amazon Redshift.

## Helpful links

- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-tables.html)
- [Amazon Redshift Best Practices](https://aws.amazon.com/redshift/best-practices/)

onelinerhub: [How can I design tables to optimize performance when using Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-can-i-design-tables-to-optimize-performance-when-using-amazon-redshift)