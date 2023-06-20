# How do I use Google Big Query with Java?
// plain

Google BigQuery is a serverless, highly scalable, and cost-effective cloud data warehouse that enables users to query large datasets using SQL. It can be used with Java by using the BigQuery Java Client Library. This library provides an API to access BigQuery from Java applications.

## Example code

```
// Imports the Google Cloud client library
import com.google.cloud.bigquery.BigQuery;
import com.google.cloud.bigquery.BigQueryOptions;

// Instantiates a client
BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
```

This code creates a BigQuery client object which can then be used to execute queries and other operations. For example, the following code executes a query to find the top 10 most popular words in a table:
```
// The SQL query to run
String query = "SELECT word, word_count FROM `bigquery-public-data.samples.shakespeare` ORDER BY word_count DESC LIMIT 10";

// Creates a query job
Job job = bigquery.create(JobInfo.of(QueryJobConfiguration.of(query)));

// Waits for the query to complete
job = job.waitFor();

// Prints the results
TableResult result = job.getQueryResults();

// Prints the results
for (FieldValueList row : result.iterateAll()) {
  String word = row.get("word").getStringValue();
  long wordCount = row.get("word_count").getLongValue();
  System.out.printf("word: %s, count: %d%n", word, wordCount);
}
```

## Output example

```
word: the, count: 27378
word: and, count: 26063
word: I, count: 20681
word: to, count: 19261
word: of, count: 18289
word: a, count: 14667
word: you, count: 13617
word: my, count: 12481
word: in, count: 10977
word: that, count: 10090
```

The code consists of the following parts:

1. **Importing the BigQuery client library** - The BigQuery Java client library is imported using `import com.google.cloud.bigquery.BigQuery;` and `import com.google.cloud.bigquery.BigQueryOptions;`.

2. **Creating a BigQuery client object** - A BigQuery client object is created using `BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();`.

3. **Executing a query** - The query is executed using `Job job = bigquery.create(JobInfo.of(QueryJobConfiguration.of(query)));` and `job = job.waitFor();`.

4. **Printing the results** - The results are printed using a `for` loop and the `TableResult` object.

For more information, see the [BigQuery Java Client Library documentation](https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-java) and the [BigQuery Java API reference](https://googleapis.dev/java/google-cloud-clients/latest/index.html).

onelinerhub: [How do I use Google Big Query with Java?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-with-java)