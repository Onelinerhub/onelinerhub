# How do I use the Google BigQuery API with Java?
// plain

The Google BigQuery API can be used with Java to access and manipulate data stored in Google BigQuery. To get started, you will need to set up the necessary credentials and libraries.

1. Set up credentials:

* Go to the [Google Cloud Platform Console](https://console.cloud.google.com/) and create a project, or use an existing one.
* Enable the [BigQuery API](https://console.cloud.google.com/apis/library/bigquery.googleapis.com).
* Create a [service account](https://cloud.google.com/iam/docs/service-accounts) and download the JSON file with the credentials.

2. Install the Java BigQuery client library:

* Add the following line to your `pom.xml` file:
```xml
<dependency>
    <groupId>com.google.cloud</groupId>
    <artifactId>google-cloud-bigquery</artifactId>
    <version>1.94.0</version>
</dependency>
```
* Install the library with Maven:
```
mvn install
```

3. Use the Java BigQuery client library:

* Create a `BigQuery` object with the credentials file:
```java
BigQuery bigquery = BigQueryOptions.newBuilder().setCredentials(credentials).build().getService();
```
* Run a query:
```java
String query = "SELECT word FROM `bigquery-public-data.samples.shakespeare` GROUP BY word;";
QueryJobConfiguration queryConfig = QueryJobConfiguration.newBuilder(query).build();
// Create a job ID so that we can safely retry.
JobId jobId = JobId.of(UUID.randomUUID().toString());
Job queryJob = bigquery.create(JobInfo.newBuilder(queryConfig).setJobId(jobId).build());
// Wait for the query to complete.
queryJob = queryJob.waitFor();
// Check for errors
if (queryJob == null) {
    throw new RuntimeException("Job no longer exists");
} else if (queryJob.getStatus().getError() != null) {
    // You can also look at queryJob.getStatus().getExecutionErrors() for all
    // errors, not just the latest one.
    throw new RuntimeException(queryJob.getStatus().getError().toString());
}
// Get the results.
TableResult result = queryJob.getQueryResults();
```
* Print the results:
```java
for (FieldValueList row : result.iterateAll()) {
    String word = row.get("word").getStringValue();
    System.out.println("word: " + word);
}
```

## Output example

```
word: A
word: All
word: Am
word: ...
```

For more information, see the [BigQuery Java API reference](https://googleapis.dev/java/google-cloud-clients/latest/com/google/cloud/bigquery/package-summary.html).

onelinerhub: [How do I use the Google BigQuery API with Java?](https://onelinerhub.com/google-big-query/how-do-i-use-the-google-bigquery-api-with-java)