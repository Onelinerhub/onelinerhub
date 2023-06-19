# How can I obtain Google BigQuery certification?
// plain

Google BigQuery certification is designed to demonstrate proficiency in the Google BigQuery platform. To obtain certification, you must pass the Google Cloud Certified Professional Data Engineer exam.

The exam consists of multiple choice questions and hands-on tasks. The hands-on tasks require you to write and execute SQL queries on a live BigQuery instance.

To prepare for the exam, you should review the official exam guide and practice writing and executing SQL queries on a BigQuery instance. You can find sample questions and practice tasks [here](https://cloud.google.com/certification/guides/data-engineer/).

You can also use the following example code to practice querying data in BigQuery. This example queries the public `bigquery-public-data.usa_names.usa_1910_current` table to find the top 10 most popular first names in the US in 2018.

```
SELECT name, SUM(number) AS total
FROM `bigquery-public-data.usa_names.usa_1910_current`
WHERE year = 2018
GROUP BY name
ORDER BY total DESC
LIMIT 10
```

The output of this query is a list of the top 10 most popular first names in the US in 2018 and the total number of people with each name:

```
name	total
James	507344
John	505931
Robert	488825
Michael	437313
Mary	413127
William	403749
David	351426
Joseph	266744
Richard	266692
Charles	255326
```

Once you have practiced and feel confident, you can register for the exam [here](https://cloud.google.com/certification/data-engineer).

onelinerhub: [How can I obtain Google BigQuery certification?](https://onelinerhub.com/google-big-query/how-can-i-obtain-google-bigquery-certification)