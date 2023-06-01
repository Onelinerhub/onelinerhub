# How do I use the PHP SDK for AWS?
// plain

The PHP SDK for AWS allows developers to access and interact with AWS services such as Amazon S3, Amazon EC2, and Amazon DynamoDB. To use the SDK, you must first install the AWS SDK for PHP via Composer or by downloading the source code.

Once the SDK is installed, you can start using it to interact with AWS services. For example, to list all buckets in an Amazon S3 account, you can use the following code:

```php
<?php
// Include the SDK
require 'vendor/autoload.php';

// Create an S3 client
$s3 = new Aws\S3\S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);

// List all buckets
$result = $s3->listBuckets();

foreach ($result['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

This code will output a list of all buckets in the Amazon S3 account.

The code consists of the following parts:

1. `require 'vendor/autoload.php'` - This line loads the AWS SDK for PHP.
2. `$s3 = new Aws\S3\S3Client([])` - This line creates an S3 client object.
3. `$result = $s3->listBuckets()` - This line lists all buckets in the Amazon S3 account.
4. `foreach ($result['Buckets'] as $bucket)` - This loop iterates through the list of buckets and prints out each bucket name.

For more information on using the AWS SDK for PHP, please refer to the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/).

onelinerhub: [How do I use the PHP SDK for AWS?](https://onelinerhub.com/php-aws/how-do-i-use-the-php-sdk-for-aws)