# How do I write a file to an AWS S3 bucket using PHP?
// plain

Writing a file to an AWS S3 bucket using PHP is a simple process. Here is an example code block to demonstrate the process:

```
// Include the AWS SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create an S3 client
$s3 = new Aws\S3\S3Client([
    'region'  => 'us-west-2',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'YourAccessKeyId',
        'secret' => 'YourSecretAccessKey',
    ]
]);

// Upload a file
$result = $s3->putObject([
    'Bucket' => 'YourBucketName',
    'Key'    => 'YourFileName.txt',
    'Body'   => 'This is the content of the file.'
]);

// Print the URL to the object
echo $result['ObjectURL'] . "\n";
```

The code above will create an S3 client using the credentials provided, upload a file to the specified S3 bucket, and print out the URL to the object.

The code consists of the following parts:

1. `require 'vendor/autoload.php'`: This line will include the AWS SDK using the Composer autoloader.
2. `$s3 = new Aws\S3\S3Client([])`: This line will create an S3 client using the credentials provided.
3. `$result = $s3->putObject([])`: This line will upload a file to the specified S3 bucket.
4. `echo $result['ObjectURL']`: This line will print out the URL to the object.

For more information on writing files to an AWS S3 bucket using PHP, please refer to the following links:

* [Uploading Objects Using the AWS SDK for PHP](https://docs.aws.amazon.com/AmazonS3/latest/dev/UploadObjSingleOpPHP.html)
* [Using the AWS SDK for PHP with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingPHPSDK.html)

onelinerhub: [How do I write a file to an AWS S3 bucket using PHP?](https://onelinerhub.com/php-aws/how-do-i-write-a-file-to-an-aws-s--bucket-using-php)