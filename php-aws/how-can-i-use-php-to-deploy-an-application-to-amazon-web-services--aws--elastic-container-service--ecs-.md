# How can I use PHP to deploy an application to Amazon Web Services (AWS) Elastic Container Service (ECS)?
// plain

PHP can be used to deploy an application to Amazon Web Services (AWS) Elastic Container Service (ECS) by making use of the AWS SDK for PHP. The following example code can be used to create a new ECS cluster:

```
<?php

require 'vendor/autoload.php';

use Aws\Ecs\EcsClient;

$client = new EcsClient([
    'region'  => 'us-east-1',
    'version' => 'latest'
]);

$result = $client->createCluster([
    'clusterName' => 'my-ecs-cluster',
]);

echo $result['cluster']['clusterArn'];

?>
```

The output of the example code will be the ARN of the newly created cluster.

## Code explanation


1. `require 'vendor/autoload.php';`: This line includes the autoloader which is used to load the AWS SDK for PHP.

2. `use Aws\Ecs\EcsClient;`: This line includes the ECS client which is used to interact with the ECS service.

3. `$client = new EcsClient([`: This line creates a new ECS client which is used to interact with the ECS service.

4. `'region'  => 'us-east-1',`: This line sets the region of the ECS cluster to be created.

5. `'version' => 'latest'`: This line sets the version of the ECS client to be used.

6. `$result = $client->createCluster([`: This line creates a new ECS cluster.

7. `'clusterName' => 'my-ecs-cluster',`: This line sets the name of the ECS cluster to be created.

8. `echo $result['cluster']['clusterArn'];`: This line prints the ARN of the newly created cluster.

## Helpful links

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [AWS ECS Client](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Ecs.EcsClient.html)

onelinerhub: [How can I use PHP to deploy an application to Amazon Web Services (AWS) Elastic Container Service (ECS)?](https://onelinerhub.com/php-aws/how-can-i-use-php-to-deploy-an-application-to-amazon-web-services--aws--elastic-container-service--ecs-)