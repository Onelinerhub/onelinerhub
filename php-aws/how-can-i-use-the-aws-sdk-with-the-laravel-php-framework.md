# How can I use the AWS SDK with the Laravel PHP framework?
// plain

The AWS SDK can be used with the Laravel PHP framework via the AWS SDK for PHP library. This library provides APIs for working with Amazon Web Services such as S3, DynamoDB, and more.

To use the AWS SDK with Laravel, you will first need to install the AWS SDK for PHP library via Composer. This can be done by running the following command in your terminal:

```
composer require aws/aws-sdk-php
```

Once the library is installed, you will need to configure the AWS SDK for PHP. This can be done by adding the following code to your Laravel configuration file:

```
'aws' => [
    'key'    => 'Your AWS Access Key',
    'secret' => 'Your AWS Secret Key',
    'region' => 'Your AWS Region',
],
```

Once the configuration is complete, you can use the AWS SDK for PHP to make API calls. For example, the following code will list all the buckets in your S3 account:

```
use Aws\S3\S3Client;

$s3 = new S3Client([
    'region'  => 'Your AWS Region',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'Your AWS Access Key',
        'secret' => 'Your AWS Secret Key',
    ]
]);

$buckets = $s3->listBuckets();

foreach ($buckets['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

## Output example

```
my-bucket-1
my-bucket-2
my-bucket-3
```

- `composer require aws/aws-sdk-php`: Installs the AWS SDK for PHP library via Composer.
- `'aws' => [ ... ]`: Configures the AWS SDK for PHP.
- `$s3 = new S3Client([ ... ])`: Creates an S3Client object.
- `$buckets = $s3->listBuckets()`: Lists all the buckets in your S3 account.
- `echo $bucket['Name'] . "\n"`: Outputs the name of each bucket.

## Helpful links
- [AWS SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_installation.html)
- [Laravel Documentation](https://laravel.com/docs/7.x/installation)

onelinerhub: [How can I use the AWS SDK with the Laravel PHP framework?](https://onelinerhub.com/php-aws/how-can-i-use-the-aws-sdk-with-the-laravel-php-framework)