# How do I use the PHP AWS S3 Client?
// plain

The PHP AWS S3 Client is a library that provides an easy way to interact with Amazon Web Services (AWS) Simple Storage Service (S3). It enables developers to store and retrieve data from S3 buckets.

To use this client, first you need to install the AWS SDK for PHP using Composer by running the following command:

```
composer require aws/aws-sdk-php
```

Once the SDK is installed, you can create an instance of the S3 client:

```php
$s3Client = new Aws\S3\S3Client([
    'region'  => 'us-east-1',
    'version' => 'latest'
]);
```

You can then use the client to perform operations on S3 buckets. For example, to list all buckets in your account:

```php
$buckets = $s3Client->listBuckets();

// Output the bucket names
foreach ($buckets['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

The PHP AWS S3 Client also provides methods for uploading, downloading, copying, and deleting objects from S3 buckets. For more information, please refer to the [official documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html).

onelinerhub: [How do I use the PHP AWS S3 Client?](https://onelinerhub.com/php-aws/how-do-i-use-the-php-aws-s--client)