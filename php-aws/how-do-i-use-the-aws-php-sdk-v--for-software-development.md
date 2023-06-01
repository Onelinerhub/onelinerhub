# How do I use the AWS PHP SDK v2 for software development?
// plain

The AWS PHP SDK v2 is a library that enables developers to build applications that interact with Amazon Web Services (AWS). To use the SDK, you will need to install the AWS PHP SDK v2 via composer.

Once the SDK is installed, you can begin using it in your application. Here is an example of how to use the SDK to list the buckets in an AWS S3 account:

```php
// Include the AWS SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create an Amazon S3 client
$s3Client = new Aws\S3\S3Client([
    'region'  => 'us-east-1',
    'version' => 'latest'
]);

// List the buckets in the account
$buckets = $s3Client->listBuckets();

foreach ($buckets['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

The above code will output a list of bucket names:

```
my-bucket-1
my-bucket-2
my-bucket-3
```

## Code explanation


* `require 'vendor/autoload.php'` - This line includes the AWS PHP SDK v2 using the Composer autoloader.
* `$s3Client = new Aws\S3\S3Client([])` - This line creates an Amazon S3 client.
* `$buckets = $s3Client->listBuckets()` - This line lists the buckets in the account.
* `foreach ($buckets['Buckets'] as $bucket)` - This loop iterates over the buckets and prints out their names.

For more information, please refer to the [AWS PHP SDK v2 Documentation](https://docs.aws.amazon.com/aws-sdk-php/v2/guide/).

onelinerhub: [How do I use the AWS PHP SDK v2 for software development?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-php-sdk-v--for-software-development)