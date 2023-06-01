# How do I use the AWS PHP SDK to set up an IAM role?
// plain

1. First, install the AWS PHP SDK using Composer:
```
composer require aws/aws-sdk-php
```

2. Next, create an IAM role using the AWS PHP SDK. You can do this by creating an `Aws\Iam\IamClient` object and calling the `createRole` method on it.

```
$client = new Aws\Iam\IamClient([
    'region'  => 'us-east-1',
    'version' => '2010-05-08',
]);

$result = $client->createRole([
    'AssumeRolePolicyDocument' => '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }',
    'RoleName' => 'my-iam-role',
]);
```

3. The output of the above code will be an `Aws\Result` object containing the details of the created IAM role.

```
Aws\Result Object
(
    [data:Aws\Result:private] => Array
        (
            [Role] => Array
                (
                    [Path] => /
                    [RoleName] => my-iam-role
                    [RoleId] => AROAJ6I4X3KXGJTJX5NCK
                    [Arn] => arn:aws:iam::123456789012:role/my-iam-role
                    [CreateDate] => 2020-08-05T20:30:27.000Z
                    [AssumeRolePolicyDocument] => {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Principal": {
                                    "Service": "ec2.amazonaws.com"
                                },
                                "Action": "sts:AssumeRole"
                            }
                        ]
                    }
                )
        )
)
```

4. You can also add permissions to the IAM role by calling the `putRolePolicy` method on the `Aws\Iam\IamClient` object.

```
$client->putRolePolicy([
    'PolicyDocument' => '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:ListBucket",
                "Resource": "arn:aws:s3:::my-bucket"
            }
        ]
    }',
    'RoleName' => 'my-iam-role',
    'PolicyName' => 'MyBucketPolicy',
]);
```

5. You can also delete the IAM role by calling the `deleteRole` method on the `Aws\Iam\IamClient` object.

```
$client->deleteRole([
    'RoleName' => 'my-iam-role',
]);
```

6. For more information about using the AWS PHP SDK to manage IAM roles, refer to the [AWS PHP SDK Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Iam.IamClient.html).

7. You can also refer to the [AWS IAM Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) for more information about IAM roles.

onelinerhub: [How do I use the AWS PHP SDK to set up an IAM role?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-php-sdk-to-set-up-an-iam-role)