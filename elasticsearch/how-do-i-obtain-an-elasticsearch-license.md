# How do I obtain an elasticsearch license?
// plain

The easiest way to obtain an Elasticsearch license is to purchase a subscription from the Elastic website. Depending on your needs, you can select from Basic, Gold, Platinum, and Enterprise tiers.

You can also obtain a license by running the following command on the command line:

```
curl -XGET 'https://elastic:<password>@<host>:9200/_xpack/license'
```

This command will return the license information associated with the cluster, including the type of license, expiry date, and other details.

## Code explanation


* `curl -XGET`: This is a command to make a GET request using the `curl` command.
* `https://elastic:<password>@<host>:9200/_xpack/license`: This is the URL of the license endpoint. You need to replace `<password>` and `<host>` with the appropriate values for your cluster.
* `_xpack/license`: This is the endpoint for retrieving the license information associated with the cluster.

For more information, please refer to the [Elasticsearch License Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/license.html).

onelinerhub: [How do I obtain an elasticsearch license?](https://onelinerhub.com/elasticsearch/how-do-i-obtain-an-elasticsearch-license)