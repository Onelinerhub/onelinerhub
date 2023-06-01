# How do I use PHP to get a file from AWS S3?
// plain

Using PHP to get a file from AWS S3 is easy. The following example code block will demonstrate how to do this:

```
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create an S3Client
$s3Client = new Aws\S3\S3Client([
    'region'  => 'us-east-1',
    'version' => '2006-03-01'
]);

// Get the object
$result = $s3Client->getObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-file.jpg'
]);

// Print the body of the object
echo $result['Body'];
```

The above code includes the following parts:

1. Include the SDK using the Composer autoloader
2. Create an S3Client
3. Get the object
4. Print the body of the object

The first part includes the SDK using the Composer autoloader. The second part creates an S3Client that will be used to access the object. The third part gets the object from the given bucket and key. The fourth part prints the body of the object.

## Helpful links

- [Getting Started with the AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/basic-usage.html)
- [Amazon S3 PHP Examples](https://docs.aws.amazon.com/AmazonS3/latest/dev/ExamplesPHP.html)

onelinerhub: [How do I use PHP to get a file from AWS S3?](https://onelinerhub.com/php-aws/how-do-i-use-php-to-get-a-file-from-aws-s-)