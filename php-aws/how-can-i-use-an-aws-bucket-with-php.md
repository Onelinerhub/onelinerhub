# How can I use an AWS bucket with PHP?
// plain

Using an AWS bucket with PHP is a fairly straightforward process. The following code block provides an example of how to do this:
```
<?php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

$s3 = new Aws\S3\S3Client([
    'version'     => 'latest',
    'region'      => 'us-east-1',
    'credentials' => [
        'key'    => 'your-access-key-here',
        'secret' => 'your-secret-key-here',
    ],
]);

// Use an AWS S3 bucket
$result = $s3->putObject([
    'Bucket' => 'my-bucket-name',
    'Key'    => 'my-object-key',
    'Body'   => 'this is the body!'
]);

// Print the URL to the object
echo $result['ObjectURL'] . "\n";
```
The output of this code would be a URL to the object stored in the S3 bucket.

The code can be broken down into the following parts:
1. The first line of code `require 'vendor/autoload.php';` is used to include the AWS SDK for PHP.
2. The next block of code is used to create an S3Client object, which is used to interact with the S3 bucket. It requires the version, region, and credentials for the S3 bucket.
3. The `putObject` function is then used to put an object into the bucket. It requires the bucket name, the object key, and the body of the object.
4. The last line of code `echo $result['ObjectURL'] . "\n";` is used to print the URL of the object stored in the S3 bucket.

For more information on how to use the AWS SDK for PHP with S3 buckets, please see the [AWS S3 documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html).

onelinerhub: [How can I use an AWS bucket with PHP?](https://onelinerhub.com/php-aws/how-can-i-use-an-aws-bucket-with-php)