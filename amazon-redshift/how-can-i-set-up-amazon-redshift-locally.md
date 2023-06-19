# How can I set up Amazon Redshift locally?
// plain

Setting up Amazon Redshift locally can be done by using the AWS CLI. To do this, first install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and configure it with your AWS credentials.

Once the AWS CLI is installed, you can create a local Amazon Redshift cluster using the following command:

```
aws redshift create-cluster --cluster-identifier <cluster-name> --node-type <node-type> --master-username <username> --master-user-password <password>
```

This command will create a cluster with the specified name, node type, username, and password. The output of this command will be a JSON object containing information about the newly created cluster.

You can also use the AWS CLI to delete the cluster when you are done with it. To do this, use the following command:

```
aws redshift delete-cluster --cluster-identifier <cluster-name>
```

This command will delete the cluster with the specified name. The output of this command will be a JSON object containing information about the deleted cluster.

For more information, please refer to the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/reference/redshift/index.html).

onelinerhub: [How can I set up Amazon Redshift locally?](https://onelinerhub.com/amazon-redshift/how-can-i-set-up-amazon-redshift-locally)