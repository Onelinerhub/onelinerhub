# How do I generate a signed URL for an AWS S3 bucket using PHP?
// plain

Generating a signed URL for an AWS S3 bucket using PHP requires the use of the AWS SDK for PHP. The following code example creates a signed URL for an S3 bucket object:

```php
// Include the AWS SDK for PHP
require 'vendor/autoload.php';

// Instantiate an Amazon S3 client
$s3Client = new Aws\S3\S3Client([
    'region'  => 'us-east-1',
    'version' => 'latest'
]);

// Create a signed URL for the object
$cmd = $s3Client->getCommand('getObject', [
    'Bucket' => 'my-bucket',
    'Key'    => 'my-object'
]);
$request = $s3Client->createPresignedRequest($cmd, '+20 minutes');
$signedUrl = (string)$request->getUri();

echo $signedUrl;
```

## Output example


```
https://my-bucket.s3.amazonaws.com/my-object?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Expires=1583258320&Signature=D6F3DAF5D4F6D5F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6
```

The code:
1. Includes the AWS SDK for PHP (`require 'vendor/autoload.php'`)
2. Instantiates an Amazon S3 client (`$s3Client = new Aws\S3\S3Client([ ... ])`)
3. Creates a signed URL for the object (`$cmd = $s3Client->getCommand('getObject', [ ... ])`)
4. Generates the pre-signed request (`$request = $s3Client->createPresignedRequest($cmd, '+20 minutes')`)
5. Retrieves the signed URL (`$signedUrl = (string)$request->getUri()`)
6. Prints the signed URL (`echo $signedUrl`)

## Helpful links
- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [Amazon S3 client](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)
- [getObject](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getobject)
- [createPresignedRequest](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html#_createPresignedRequest)

onelinerhub: [How do I generate a signed URL for an AWS S3 bucket using PHP?](https://onelinerhub.com/php-aws/how-do-i-generate-a-signed-url-for-an-aws-s--bucket-using-php)