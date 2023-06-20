# How can I use Google Big Query with GitHub?
// plain

Google BigQuery can be used with GitHub in several ways.

First, BigQuery can be used to query and analyze public GitHub data. GitHub publishes a public dataset of all GitHub events, which can be accessed in BigQuery. This dataset includes data such as pull requests, commits, and issues. For example, the following query can be used to count the number of commits per repository:

```
SELECT repository.name, COUNT(*) AS num_commits
FROM `githubarchive.month.20*`
WHERE type="PushEvent"
GROUP BY repository.name
```

This query will return a list of repositories, along with the number of commits to each one.

Second, BigQuery can be used to store and analyze private data from GitHub. This can be done by connecting BigQuery to GitHub's API. With this connection, data from GitHub repositories can be exported to BigQuery for further analysis.

Finally, BigQuery can be used to integrate with GitHub Actions. GitHub Actions is a feature of GitHub that allows users to automate tasks. With BigQuery, users can trigger actions based on data stored in BigQuery. For example, a user can set up an action to automatically send an email when certain conditions in BigQuery are met.

In summary, Google BigQuery can be used with GitHub in several ways, including querying public datasets, storing and analyzing private data, and integrating with GitHub Actions.

## Helpful links
- [GitHub Public Dataset](https://www.githubarchive.org/)
- [Connecting BigQuery to GitHub's API](https://cloud.google.com/solutions/connecting-github-and-bigquery)
- [GitHub Actions](https://help.github.com/en/actions)

onelinerhub: [How can I use Google Big Query with GitHub?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-with-github)