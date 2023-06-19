# How can I take a course on Google Big Query?
// plain

If you are interested in taking a course on Google Big Query, there are a variety of resources available.

One of the best ways to learn is by joining a course offered by Google. Google offers an online course called “Google Cloud Platform Big Data and Machine Learning Fundamentals” that covers the fundamentals of Big Query. The course is free and can be completed in about 8 hours.

You can also learn Big Query by taking an online course from a third-party provider. Udemy offers an online course called “Google BigQuery: Data Analysis & Visualization” which covers topics such as data modeling, querying, and visualization.

If you prefer to learn through hands-on experience, you can use Big Query in the Google Cloud Platform. To get started, you will need to create a Google Cloud Platform account and enable the Big Query API. Once you have done that, you can use the Big Query web interface or the command line tool to query data and create tables.

For example, the following code will create a table called “mytable” in the “mydataset” dataset:

```
bq mk --table mydataset.mytable
```

You can also use Big Query with Python. The following code will query data from the “mytable” table:

```
from google.cloud import bigquery

client = bigquery.Client()

query = "SELECT * FROM mydataset.mytable"

query_job = client.query(query)

for row in query_job:
    print(row)
```

## Output example


```
Row(('value1', 'value2'))
```

For more information on Google Big Query, you can refer to the official documentation [here](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How can I take a course on Google Big Query?](https://onelinerhub.com/google-big-query/how-can-i-take-a-course-on-google-big-query)