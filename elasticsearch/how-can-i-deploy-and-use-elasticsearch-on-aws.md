# How can I deploy and use Elasticsearch on AWS?
// plain

Deploying and using Elasticsearch on AWS can be done in several steps:

1. Create an Elasticsearch domain in the AWS Elasticsearch Service.
```
aws es create-elasticsearch-domain --domain-name my-domain
```

2. Configure the cluster using the AWS CLI.
```
aws es update-elasticsearch-domain-config \
  --domain-name my-domain \
  --elasticsearch-cluster-config InstanceType=m3.medium.elasticsearch,InstanceCount=2
```

3. Create an IAM policy and role for the Elasticsearch domain.
```
aws iam create-policy --policy-name my-domain-policy \
  --policy-document file://my-domain-policy.json

aws iam create-role --role-name my-domain-role \
  --assume-role-policy-document file://my-domain-trust-policy.json

aws iam attach-role-policy --role-name my-domain-role \
  --policy-arn arn:aws:iam::123456789012:policy/my-domain-policy
```

4. Associate the IAM policy and role with the Elasticsearch domain.
```
aws es update-elasticsearch-domain-config \
  --domain-name my-domain \
  --access-policies file://my-domain-access-policy.json
```

5. Connect to the Elasticsearch domain using the AWS CLI.
```
aws es describe-elasticsearch-domain --domain-name my-domain
```

6. Use the Elasticsearch APIs to index and search documents.

7. Monitor the health of your domain using the AWS Management Console or the AWS CLI.

## Helpful links
- [AWS Elasticsearch Service Documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/what-is-amazon-elasticsearch-service.html)
- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

onelinerhub: [How can I deploy and use Elasticsearch on AWS?](https://onelinerhub.com/elasticsearch/how-can-i-deploy-and-use-elasticsearch-on-aws)