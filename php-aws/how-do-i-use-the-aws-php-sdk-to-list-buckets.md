# How do I use the AWS PHP SDK to list buckets?
// plain

The AWS PHP SDK provides an easy way to list buckets using the `listBuckets()` method.

The following example code will list all buckets associated with the current AWS account:

```php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create an S3 client
$s3 = new Aws\S3\S3Client([
    'version'     => 'latest',
    'region'      => 'us-east-1',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ],
]);

// List all buckets
$buckets = $s3->listBuckets();

// Output the bucket names
foreach ($buckets['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

The above code will output a list of bucket names associated with the AWS account, such as:
```
bucket-1
bucket-2
bucket-3
```

The `listBuckets()` method accepts an array of parameters (optional) to filter the list of buckets. For more information, see the [AWS PHP SDK documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#listbuckets).

onelinerhub: [How do I use the AWS PHP SDK to list buckets?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-php-sdk-to-list-buckets)