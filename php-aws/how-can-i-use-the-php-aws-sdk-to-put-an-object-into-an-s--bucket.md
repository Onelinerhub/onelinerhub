# How can I use the PHP AWS SDK to put an object into an S3 bucket?
// plain

The [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/installation.html) provides a set of libraries to interact with Amazon Web Services (AWS) services, such as S3. To put an object into an S3 bucket, use the `putObject` method from the `Aws\S3\S3Client` class.

## Example code

```php
<?php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create an S3Client
$s3Client = new Aws\S3\S3Client([
    'region'  => 'us-west-2',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ]
]);

// Upload an object
$result = $s3Client->putObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-object',
    'Body'   => 'this is the body!'
]);

echo $result['ObjectURL'];
```

## Output example

```
https://my-bucket.s3.amazonaws.com/my-object
```

The code above does the following:

1. Includes the SDK using the Composer autoloader.
2. Creates an S3Client using the provided credentials.
3. Uploads an object to a specified bucket using the putObject method.
4. Prints the ObjectURL of the uploaded object.

## Helpful links
- [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/installation.html)
- [putObject](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putobject)

onelinerhub: [How can I use the PHP AWS SDK to put an object into an S3 bucket?](https://onelinerhub.com/php-aws/how-can-i-use-the-php-aws-sdk-to-put-an-object-into-an-s--bucket)