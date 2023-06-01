# How can I use AWS to get results from a PHP application?
// plain

You can use AWS to get results from a PHP application by using the AWS SDK for PHP. The SDK provides a set of classes that allow you to interact with various AWS services, such as Amazon S3, Amazon DynamoDB, and Amazon EC2.

For example, you can use the SDK to get the list of objects in an Amazon S3 bucket:

```php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Use the us-east-1 region and latest version of each client.
$sharedConfig = [
    'region'  => 'us-east-1',
    'version' => 'latest'
];

// Create an SDK class used to share configuration across clients.
$sdk = new Aws\Sdk($sharedConfig);

// Create an Amazon S3 client using the shared configuration data.
$s3Client = $sdk->createS3();

// Get the list of objects in the specified Amazon S3 bucket.
$result = $s3Client->listObjects([
    'Bucket' => 'my-bucket-name'
]);

// Print the list of objects.
print_r($result);
```

## Output example


```
Array
(
    [Contents] => Array
        (
            [0] => Array
                (
                    [Key] => filename1.txt
                    [LastModified] => 2020-03-02T12:34:56+00:00
                    [Size] => 12345
                )

            [1] => Array
                (
                    [Key] => filename2.txt
                    [LastModified] => 2020-03-02T12:34:56+00:00
                    [Size] => 12345
                )
        )
)
```

## Code explanation


- `require 'vendor/autoload.php';`: Includes the SDK using the Composer autoloader.
- `$sharedConfig = [ 'region'  => 'us-east-1', 'version' => 'latest' ];`: Defines the region and version of the AWS services.
- `$sdk = new Aws\Sdk($sharedConfig);`: Creates an SDK class used to share configuration across clients.
- `$s3Client = $sdk->createS3();`: Creates an Amazon S3 client using the shared configuration data.
- `$result = $s3Client->listObjects([ 'Bucket' => 'my-bucket-name' ]);`: Gets the list of objects in the specified Amazon S3 bucket.
- `print_r($result);`: Prints the list of objects.

## Helpful links

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [Getting Started with the AWS SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started.html)
- [Amazon S3 Client](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)

onelinerhub: [How can I use AWS to get results from a PHP application?](https://onelinerhub.com/php-aws/how-can-i-use-aws-to-get-results-from-a-php-application)