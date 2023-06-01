# How do I use the AWS SDK for PHP to get an object from an S3 bucket?
// plain

Using the AWS SDK for PHP to get an object from an S3 bucket is a straightforward process. The following is an example of how to do this:

```php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create an S3Client
$s3Client = new Aws\S3\S3Client([
    'region'  => 'us-west-2',
    'version' => 'latest',
    'scheme' => 'http'
]);

// Get an object
$result = $s3Client->getObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-object'
]);

// Print the body of the object
echo $result['Body'];
```

The code above will print out the body of the object.

The code consists of the following parts:

1. Include the SDK using the Composer autoloader
2. Create an S3Client
3. Get an object
4. Print the body of the object

The S3Client is instantiated with the region, version, and scheme. The getObject() method is then used to get the object from the S3 bucket. Finally, the body of the object is printed out.

## Helpful links

- [AWS SDK for PHP Documentation](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_basic-usage.html)
- [AWS S3Client Class](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)
- [AWS getObject() Function](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getobject)

onelinerhub: [How do I use the AWS SDK for PHP to get an object from an S3 bucket?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-sdk-for-php-to-get-an-object-from-an-s--bucket)