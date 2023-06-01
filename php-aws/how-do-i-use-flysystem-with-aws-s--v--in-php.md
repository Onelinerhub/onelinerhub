# How do I use Flysystem with AWS S3 v3 in PHP?
// plain

Flysystem is a filesystem abstraction library for PHP that allows you to use different storage systems, such as AWS S3 v3, as if they were a local filesystem. To use Flysystem with AWS S3 v3 in PHP, you need to install the Flysystem library and the AWS SDK for PHP.

Once you have both libraries installed, you can use the following code to connect to your S3 bucket:
```php
use Aws\S3\S3Client;
use League\Flysystem\AwsS3v3\AwsS3Adapter;

$client = new S3Client([
    'credentials' => [
        'key'    => 'YOUR_AWS_KEY',
        'secret' => 'YOUR_AWS_SECRET',
    ],
    'region' => 'YOUR_AWS_REGION',
    'version' => 'latest',
]);

$adapter = new AwsS3Adapter($client, 'YOUR_BUCKET_NAME');
```
Once the adapter is created, you can use it to create a Flysystem instance and start working with the S3 bucket as if it was a local filesystem:
```php
use League\Flysystem\Filesystem;

$filesystem = new Filesystem($adapter);
```

You can then use the `$filesystem` instance to read, write, and delete files from the S3 bucket. For example, you can use the `write()` method to write a file to the S3 bucket:
```php
$filesystem->write('path/to/file.txt', 'contents');
```

For more information, see the [Flysystem documentation](http://flysystem.thephpleague.com/v1/docs/) and the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/).

onelinerhub: [How do I use Flysystem with AWS S3 v3 in PHP?](https://onelinerhub.com/php-aws/how-do-i-use-flysystem-with-aws-s--v--in-php)