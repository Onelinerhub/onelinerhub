# How do I configure Amazon EC2 to deploy a Kubernetes cluster?
// plain

1. Create an Amazon EC2 key pair and store the private key in a secure location:
```
aws ec2 create-key-pair --key-name <key-name> --query 'KeyMaterial' --output text > <key-name>.pem
```

2. Create a security group for the Kubernetes cluster with ports 80, 443, and 6443 open for ingress traffic:
```
aws ec2 create-security-group --group-name k8s-cluster --description "Security group for Kubernetes cluster"
aws ec2 authorize-security-group-ingress --group-name k8s-cluster --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name k8s-cluster --protocol tcp --port 443 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name k8s-cluster --protocol tcp --port 6443 --cidr 0.0.0.0/0
```

3. Create an IAM role for the EC2 instances in the Kubernetes cluster:
```
aws iam create-role --role-name k8s-cluster-role --assume-role-policy-document file://k8s-cluster-role-trust-policy.json
```

4. Create a CloudFormation stack to deploy the Kubernetes cluster:
```
aws cloudformation create-stack --stack-name k8s-cluster --template-body file://k8s-cluster-template.yaml --parameters ParameterKey=KeyName,ParameterValue=<key-name> ParameterKey=SecurityGroupId,ParameterValue=<security-group-id> ParameterKey=RoleArn,ParameterValue=<role-arn>
```

5. Monitor the progress of the CloudFormation stack:
```
aws cloudformation describe-stacks --stack-name k8s-cluster
```

6. Once the stack has been successfully created, the Kubernetes cluster should be up and running.

7. To access the Kubernetes cluster, use the kubectl command-line tool and the kubeconfig file that was created by the CloudFormation stack:
```
kubectl --kubeconfig <kubeconfig-file> get nodes
```

**Output**
```
NAME                                          STATUS   ROLES    AGE   VERSION
ip-10-0-1-123.ec2.internal                    Ready    master   4m    v1.17.4
ip-10-0-2-123.ec2.internal                    Ready    <none>   2m    v1.17.4
ip-10-0-3-123.ec2.internal                    Ready    <none>   1m    v1.17.4
```

**Explanation of Code Parts**

* `aws ec2 create-key-pair`: Creates a new Amazon EC2 key pair with the specified name.
* `aws ec2 create-security-group`: Creates a new Amazon EC2 security group with the specified name and description.
* `aws ec2 authorize-security-group-ingress`: Authorizes ingress traffic for the specified security group and port.
* `aws iam create-role`: Creates a new IAM role with the specified name and trust policy document.
* `aws cloudformation create-stack`: Creates a new CloudFormation stack with the specified name and template body.
* `aws cloudformation describe-stacks`: Retrieves information about the specified CloudFormation stack.
* `kubectl --kubeconfig`: Uses the specified kubeconfig file to access the Kubernetes cluster.

**Relevant Links**

* [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
* [Amazon EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html)
* [Amazon IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
* [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
* [Kubernetes](https://kubernetes.io/)

onelinerhub: [How do I configure Amazon EC2 to deploy a Kubernetes cluster?](https://onelinerhub.com/amazon-redshift/how-do-i-configure-amazon-ec--to-deploy-a-kubernetes-cluster)