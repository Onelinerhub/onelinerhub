# How do Amazon Redshift Spectrum and Amazon Athena compare?
// plain

Amazon Redshift Spectrum and Amazon Athena are both services that can be used to query data stored in Amazon S3. They both allow users to analyze large amounts of data without having to load it into a data warehouse, but there are some key differences between the two services.

Redshift Spectrum is an extension of Amazon Redshift that allows users to query data stored in S3. It supports data stored in columnar formats such as Apache Parquet and ORC. Redshift Spectrum allows users to join data from S3 with data stored in their Amazon Redshift cluster. It also supports advanced features such as data encryption, partitioning, and query pushdown.

Amazon Athena is a serverless query service that allows users to query data stored in S3 using SQL. It supports data stored in formats such as CSV, JSON, Apache ORC, and Apache Parquet. Unlike Redshift Spectrum, Athena does not support joining data stored in S3 with data stored in other databases.

## Example code


```sql
SELECT *
FROM s3_table
WHERE col1 = 'value'
```

## Output example


```
col1 | col2 | col3
value | abc  | def
```

The main differences between Redshift Spectrum and Athena are:

1. Redshift Spectrum supports joining data stored in S3 with data stored in other databases, while Athena does not.
2. Redshift Spectrum supports advanced features such as data encryption, partitioning, and query pushdown, while Athena does not.
3. Redshift Spectrum supports columnar formats such as Apache Parquet and ORC, while Athena only supports CSV, JSON, Apache ORC, and Apache Parquet.

## Helpful links

- [Amazon Redshift Spectrum](https://aws.amazon.com/redshift/spectrum/)
- [Amazon Athena](https://aws.amazon.com/athena/)

onelinerhub: [How do Amazon Redshift Spectrum and Amazon Athena compare?](https://onelinerhub.com/amazon-redshift/how-do-amazon-redshift-spectrum-and-amazon-athena-compare)