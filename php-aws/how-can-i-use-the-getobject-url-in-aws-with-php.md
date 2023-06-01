# How can I use the GetObject URL in AWS with PHP?
// plain

The GetObject URL in AWS can be used with PHP to access objects stored in the AWS S3 bucket. You can use the following code to get the object from the bucket:

```
<?php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

$s3 = new Aws\S3\S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);

$bucket = 'my-bucket';
$key = 'my-object';

$result = $s3->getObject([
    'Bucket' => $bucket,
    'Key'    => $key
]);

echo $result['Body'];
?>
```

This code will print out the contents of the object stored in the S3 bucket.

## Code explanation


1. `require 'vendor/autoload.php';`: This line is used to include the SDK using the Composer autoloader.
2. `$s3 = new Aws\S3\S3Client([...])`: This line is used to create a new S3Client object.
3. `$bucket = 'my-bucket';`: This line is used to set the bucket name.
4. `$key = 'my-object';`: This line is used to set the object key.
5. `$result = $s3->getObject([...])`: This line is used to get the object from the bucket.
6. `echo $result['Body'];`: This line is used to print out the contents of the object.

## Helpful links

- [AWS S3 PHP SDK](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)
- [Getting an Object Using GetObject](https://docs.aws.amazon.com/AmazonS3/latest/dev/RetrieveObjSingleOpPHP.html)

onelinerhub: [How can I use the GetObject URL in AWS with PHP?](https://onelinerhub.com/php-aws/how-can-i-use-the-getobject-url-in-aws-with-php)