# How can I generate a presigned URL using the AWS PHP SDK?
// plain

Generating a presigned URL using the AWS PHP SDK is relatively straightforward. The following example code block demonstrates how to generate a presigned URL with the AWS SDK for PHP:

```
<?php
// Include the AWS SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create an Amazon S3 client object
$s3Client = new Aws\S3\S3Client([
    'version'     => 'latest',
    'region'      => 'us-west-2',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ]
]);

// Set the bucket and object name
$bucket = 'my-bucket';
$keyname = 'my-object';

// Create a pre-signed URL for a request
$cmd = $s3Client->getCommand('GetObject', [
    'Bucket' => $bucket,
    'Key'    => $keyname
]);

$request = $s3Client->createPresignedRequest($cmd, '+20 minutes');

// Get the pre-signed URL
$presignedUrl = (string) $request->getUri();

echo $presignedUrl;
```

This example code will output a presigned URL, similar to the following:

```
https://my-bucket.s3.amazonaws.com/my-object?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=YOUR_AWS_ACCESS_KEY_ID%2F20200708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200708T000000Z&X-Amz-Expires=1200&X-Amz-SignedHeaders=host&X-Amz-Signature=f5d2d7d7d7d7d7d7d7d7d7d7d7d7d7d7d7d7d7
```

The example code consists of the following parts:

1. Include the AWS SDK using the Composer autoloader.
2. Create an Amazon S3 client object.
3. Set the bucket and object name.
4. Create a pre-signed URL for a request.
5. Get the pre-signed URL.
6. Output the pre-signed URL.

For more information on generating presigned URLs with the AWS SDK for PHP, see the following documentation:

- [Create a Pre-Signed URL Using the AWS SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-presigned-urls.html)
- [Aws\S3\S3Client::createPresignedRequest](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html#_createPresignedRequest)

onelinerhub: [How can I generate a presigned URL using the AWS PHP SDK?](https://onelinerhub.com/php-aws/how-can-i-generate-a-presigned-url-using-the-aws-php-sdk)