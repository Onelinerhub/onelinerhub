# How do I set up a Google Big Query account?
// plain

1. First, you need to have a Google Cloud Platform account. If you don’t have one, you can create one [here](https://cloud.google.com/).

2. After logging in to your Google Cloud Platform account, you can set up a BigQuery account by clicking the “Activate BigQuery” button in the left menu.

3. Once you click the “Activate BigQuery” button, you will be prompted to accept the terms of service for using BigQuery.

4. After accepting the terms of service, you will be asked to create a project. A project is a container for all the resources related to a specific BigQuery project.

5. Once the project is created, you will be taken to the BigQuery console where you can start creating datasets, tables, and queries.

6. To get started, you can try running a sample query by clicking the “Run Query” button in the top right corner.

7. For example, the following query will return the first 10 rows from the public dataset `bigquery-public-data.samples.shakespeare`:

```
SELECT *
FROM `bigquery-public-data.samples.shakespeare`
LIMIT 10
```

## Output example


```
Row	word	word_count	corpus	corpus_date
1	the	27361	the_tragedy_of_hamlet	1598
2	and	26028	the_tragedy_of_hamlet	1598
3	I	20681	the_tragedy_of_hamlet	1598
4	to	19261	the_tragedy_of_hamlet	1598
5	of	18389	the_tragedy_of_hamlet	1598
6	a	14667	the_tragedy_of_hamlet	1598
7	my	12431	the_tragedy_of_hamlet	1598
8	in	10956	the_tragedy_of_hamlet	1598
9	that	9547	the_tragedy_of_hamlet	1598
10	you	9178	the_tragedy_of_hamlet	1598
```

onelinerhub: [How do I set up a Google Big Query account?](https://onelinerhub.com/google-big-query/how-do-i-set-up-a-google-big-query-account)