# How do I generate a presigned URL for an AWS S3 bucket using PHP?
// plain

Generating a presigned URL for an AWS S3 bucket using PHP can be done using the AWS SDK for PHP. This can be done by first creating an instance of the S3 client with your credentials, then using the `getCommand` method to create a command object, and finally, executing the command to generate the URL.

```php
<?php
// Include the AWS SDK for PHP
require 'vendor/autoload.php';

// Create an S3 client
$s3 = new Aws\S3\S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY'
    ]
]);

// Create a command object
$command = $s3->getCommand('getObject', [
    'Bucket' => 'my-s3-bucket',
    'Key'    => 'my-object.txt'
]);

// Create a presigned URL
$url = $s3->createPresignedRequest($command, '+20 minutes')->getUri();

echo $url;
// Output: https://my-s3-bucket.s3.amazonaws.com/my-object.txt?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Expires=1534293045&Signature=vjbyPxybdZaNmGa%2ByT272YEAiv4%3D
```

The code above creates an instance of the S3 client, creates a command object, and then creates a presigned URL using the `createPresignedRequest` method. The URL will expire in 20 minutes.

**Code parts and explanation**

1. `require 'vendor/autoload.php';` - Include the AWS SDK for PHP.
2. `$s3 = new Aws\S3\S3Client([...]);` - Create an S3 client.
3. `$command = $s3->getCommand('getObject', [...]);` - Create a command object.
4. `$url = $s3->createPresignedRequest($command, '+20 minutes')->getUri();` - Create a presigned URL that will expire in 20 minutes.

**Relevant links**

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [S3Client Class](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)
- [getCommand Method](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html#_getCommand)
- [createPresignedRequest Method](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html#_createPresignedRequest)

onelinerhub: [How do I generate a presigned URL for an AWS S3 bucket using PHP?](https://onelinerhub.com/php-aws/how-do-i-generate-a-presigned-url-for-an-aws-s--bucket-using-php)