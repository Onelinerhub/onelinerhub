# How to use AWS API with PHP?
// plain

Using the AWS API with PHP is relatively straightforward. The following example code block shows how to use the AWS SDK for PHP to list all of the buckets in an AWS account:

```php
<?php
// Include the AWS SDK using the Composer autoloader.
require 'vendor/autoload.php';

// Create an AWS service builder using your account credentials.
$aws = new Aws\Sdk([
    'region'   => 'us-east-1',
    'version'  => 'latest',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ]
]);

// Create an Amazon S3 client using the AWS service builder.
$s3Client = $aws->createS3();

// List all of the buckets in the account.
$buckets = $s3Client->listBuckets();

// Output the bucket names.
foreach ($buckets['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

The output of the above code would be a list of all of the buckets in the AWS account:

```
my-first-bucket
my-second-bucket
my-third-bucket
```

The code consists of the following parts:

1. Include the AWS SDK using the Composer autoloader.
2. Create an AWS service builder using your account credentials.
3. Create an Amazon S3 client using the AWS service builder.
4. List all of the buckets in the account.
5. Output the bucket names.

For more information on using the AWS API with PHP, please refer to the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/).

onelinerhub: [How to use AWS API with PHP?](https://onelinerhub.com/php-aws/using-aws-api-with-php)