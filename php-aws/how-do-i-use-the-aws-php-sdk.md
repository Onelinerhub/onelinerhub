# How do I use the AWS PHP SDK?
// plain

The AWS PHP SDK is a collection of libraries that allow developers to easily build applications using Amazon Web Services. The SDK includes a set of APIs that allow developers to interact with AWS services such as Amazon S3, EC2, and others.

To use the AWS PHP SDK, you need to include the SDK in your project. The easiest way to do this is to install the SDK via Composer:

```
composer require aws/aws-sdk-php
```

Once the SDK is installed, you can create an instance of an AWS service. For example, to create an instance of the S3 client:

```php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create an S3 client
$s3 = new Aws\S3\S3Client([
    'version' => 'latest',
    'region'  => 'us-west-2'
]);
```

You can then use the `$s3` instance to make requests to the S3 service. For example, to list all buckets in your account:

```php
// List all of the buckets in your account
$result = $s3->listBuckets();

echo "Buckets:\n";
foreach ($result['Buckets'] as $bucket) {
    echo "- {$bucket['Name']}\n";
}
```

## Output example


```
Buckets:
- my-bucket
- another-bucket
```

For more information on how to use the AWS PHP SDK, please see the [official documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/).

onelinerhub: [How do I use the AWS PHP SDK?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-php-sdk)