# How do I use PHP to create an application on AWS?
// plain

Using PHP to create an application on AWS is easy and straightforward. Here is an example of how to do it:

```
<?php
// Create an Amazon S3 client
$s3Client = S3Client::factory(array(
    'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
    'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    'region' => 'YOUR_AWS_REGION'
));

// Create a bucket
$s3Client->createBucket(array(
    'Bucket' => 'my-bucket'
));

// Output
Bucket "my-bucket" created
```

The code above creates an Amazon S3 client and then uses it to create a bucket.

The code consists of the following parts:
1. `$s3Client = S3Client::factory(array(...))` - creates an Amazon S3 client using the given credentials.
2. `$s3Client->createBucket(array('Bucket' => 'my-bucket'))` - creates a bucket with the given name.

For more information about using PHP to create an application on AWS, please refer to the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/).

onelinerhub: [How do I use PHP to create an application on AWS?](https://onelinerhub.com/php-aws/how-do-i-use-php-to-create-an-application-on-aws)