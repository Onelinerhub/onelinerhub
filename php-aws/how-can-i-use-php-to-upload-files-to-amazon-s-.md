# How can I use PHP to upload files to Amazon S3?
// plain

Using PHP to upload files to Amazon S3 is relatively simple. The following example code demonstrates how to do this:

```
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create a S3 client
$s3Client = new Aws\S3\S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);

// Upload a file
$result = $s3Client->putObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-file.jpg',
    'Body'   => fopen('/path/to/file.jpg', 'r'),
    'ACL'    => 'public-read'
]);
```

The code above will upload a file located at `/path/to/file.jpg` to the S3 bucket `my-bucket` with the key `my-file.jpg` and set the access control list (ACL) to `public-read`.

The code consists of the following parts:

1. `require 'vendor/autoload.php';` - This will include the SDK using the Composer autoloader.
2. `$s3Client = new Aws\S3\S3Client([...])` - This will create a S3 client with the specified parameters.
3. `$result = $s3Client->putObject([...])` - This will upload the file to the specified S3 bucket with the specified key and ACL.

For more information, please refer to the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/index.html).

onelinerhub: [How can I use PHP to upload files to Amazon S3?](https://onelinerhub.com/php-aws/how-can-i-use-php-to-upload-files-to-amazon-s-)