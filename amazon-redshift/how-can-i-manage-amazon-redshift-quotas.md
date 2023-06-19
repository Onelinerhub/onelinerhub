# How can I manage Amazon Redshift quotas?
// plain

Amazon Redshift quotas can be managed using the AWS Command Line Interface (CLI). The CLI provides commands to list, modify, and delete quotas.

For example, to list the quotas associated with an Amazon Redshift cluster, the following command can be used:
```
aws redshift describe-cluster-quotas --cluster-identifier <cluster-identifier>
```
The output of the command will be a JSON object with the list of quotas associated with the cluster.

The following command can be used to modify an existing quota:
```
aws redshift modify-cluster-quota --cluster-identifier <cluster-identifier> --quota-type <quota-type> --quota-limit <quota-limit>
```
Where `quota-type` is the type of quota to be modified, and `quota-limit` is the new limit.

The following command can be used to delete an existing quota:
```
aws redshift delete-cluster-quota --cluster-identifier <cluster-identifier> --quota-type <quota-type>
```
Where `quota-type` is the type of quota to be deleted.

For more information about managing Amazon Redshift quotas, please refer to the [AWS documentation](https://docs.aws.amazon.com/cli/latest/reference/redshift/quotas.html).

onelinerhub: [How can I manage Amazon Redshift quotas?](https://onelinerhub.com/amazon-redshift/how-can-i-manage-amazon-redshift-quotas)