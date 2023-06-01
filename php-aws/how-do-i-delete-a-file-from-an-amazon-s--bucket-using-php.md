# How do I delete a file from an Amazon S3 bucket using PHP?
// plain

To delete a file from an Amazon S3 bucket using PHP, you can use the [`deleteObject`](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html#_deleteObject) method of the AWS SDK for PHP. The following example code shows how to delete a file from a bucket.

```php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Instantiate the S3 client with your AWS credentials
$s3Client = new Aws\S3\S3Client([
    'region'  => 'us-east-1',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ],
]);

// Delete the file from the bucket
$result = $s3Client->deleteObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-file.txt',
]);

// Print the result
print_r($result);
```

The output of the above code would look like this:
```
Aws\Result Object
(
    [data:Aws\Result:private] => Array
        (
            [DeleteMarker] =>
            [VersionId] =>
            [RequestCharged] =>
            [ResponseMetadata] => Array
                (
                    [RequestId] => xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
                    [HostId] =>
                )

        )

)
```

The code can be broken down into the following parts:
1. Include the SDK using the Composer autoloader: `require 'vendor/autoload.php';`
2. Instantiate the S3 client with your AWS credentials: `$s3Client = new Aws\S3\S3Client([...])`
3. Delete the file from the bucket: `$result = $s3Client->deleteObject([...])`
4. Print the result: `print_r($result);`

For more information, please refer to the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/index.html).

onelinerhub: [How do I delete a file from an Amazon S3 bucket using PHP?](https://onelinerhub.com/php-aws/how-do-i-delete-a-file-from-an-amazon-s--bucket-using-php)