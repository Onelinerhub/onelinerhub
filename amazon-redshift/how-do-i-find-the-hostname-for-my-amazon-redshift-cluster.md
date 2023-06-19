# How do I find the hostname for my Amazon Redshift cluster?
// plain

1. To find the hostname for your Amazon Redshift cluster, you can use the `get-cluster-credentials` AWS CLI command.

2. For example, the following command will return the hostname for the cluster specified by `--cluster-identifier`:

```
aws redshift get-cluster-credentials --cluster-identifier <cluster-name> --db-user <db-user>
```

3. The output of this command will include the hostname of the cluster, as shown below:

```
{
    "DbUser": "<db-user>",
    "Expiration": "2020-06-04T17:19:02Z",
    "DbPassword": "<db-password>",
    "ClusterIdentifier": "<cluster-name>",
    "DbGroups": [],
    "DbHost": "<cluster-hostname>"
}
```

4. The `<cluster-hostname>` value in the output is the hostname of the cluster.

5. You can also find the hostname for your Amazon Redshift cluster in the AWS Management Console. In the Redshift console, select the cluster and the hostname will be displayed in the details section.

6. Additionally, you can use the `describe-clusters` AWS CLI command to get the hostname. The following command will return the hostname for the cluster specified by `--cluster-identifier`:

```
aws redshift describe-clusters --cluster-identifier <cluster-name>
```

7. The output of this command will include the hostname of the cluster, as shown below:

```
{
    "Clusters": [
        {
            "ClusterIdentifier": "<cluster-name>",
            "NodeType": "<node-type>",
            "ClusterStatus": "available",
            "Endpoint": {
                "Address": "<cluster-hostname>",
                "Port": 5439
            },
            ...
        }
    ]
}
```

The `<cluster-hostname>` value in the output is the hostname of the cluster.

## Helpful links
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/)
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html)

onelinerhub: [How do I find the hostname for my Amazon Redshift cluster?](https://onelinerhub.com/amazon-redshift/how-do-i-find-the-hostname-for-my-amazon-redshift-cluster)