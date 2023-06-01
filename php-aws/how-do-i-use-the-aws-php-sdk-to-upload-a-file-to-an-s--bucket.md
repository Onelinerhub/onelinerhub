# How do I use the AWS PHP SDK to upload a file to an S3 bucket?
// plain

The AWS PHP SDK provides an easy way to upload files to an S3 bucket. The following example code shows how to use the SDK to upload a file to an S3 bucket.

```php
<?php
// Include the AWS SDK using the Composer autoloader.
require 'vendor/autoload.php';

// Create an S3 client.
$s3 = new Aws\S3\S3Client([
    'version' => 'latest',
    'region'  => 'us-west-2'
]);

// Upload a file.
$result = $s3->putObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-object',
    'Body'   => fopen('/path/to/file', 'r+')
]);

echo $result['ObjectURL'];
```

This code will output an S3 object URL, such as `https://my-bucket.s3.amazonaws.com/my-object`.

The code consists of the following parts:

1. `require 'vendor/autoload.php'`: This line includes the AWS SDK using the Composer autoloader.
2. `$s3 = new Aws\S3\S3Client([...])`: This line creates an S3 client. The array argument contains configuration options, such as the version and region.
3. `$result = $s3->putObject([...])`: This line uploads a file to an S3 bucket. The array argument contains the bucket name, object key, and the file contents.
4. `echo $result['ObjectURL']`: This line outputs the S3 object URL.

For more information, see the [AWS PHP SDK documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/).

onelinerhub: [How do I use the AWS PHP SDK to upload a file to an S3 bucket?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-php-sdk-to-upload-a-file-to-an-s--bucket)