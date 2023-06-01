# How do I use PHP to get an object from an AWS S3 bucket?
// plain

Using the AWS SDK for PHP, you can retrieve an object from an AWS S3 bucket with the following code:

```
<?php

// Include the AWS SDK using the Composer autoloader
require 'vendor/autoload.php';

// Instantiate an AWS client
$s3 = new Aws\S3\S3Client([
    'region'  => 'us-west-2',
    'version' => 'latest',
    'signature_version' => 'v4',
    'credentials' => [
        'key'    => 'YOUR_KEY',
        'secret' => 'YOUR_SECRET',
    ]
]);

// Retrieve the object
$result = $s3->getObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-object'
]);

// Access the object
echo $result['Body'];

```

This code will output the contents of the object stored in the `my-bucket` S3 bucket with the key `my-object`.

The code consists of the following parts:

1. **Including the AWS SDK using the Composer autoloader**: This part of the code includes the AWS SDK using the Composer autoloader. The SDK is a library that provides access to the AWS services.

2. **Instantiating an AWS client**: This part of the code instantiates an AWS client. This client can be used to access the AWS services.

3. **Retrieving the object**: This part of the code uses the AWS client to retrieve the object from the S3 bucket. The `Bucket` and `Key` parameters specify the bucket name and object key.

4. **Accessing the object**: This part of the code accesses the object and prints out its contents.

For more information, see the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/index.html) and the [Getting an Object Using the AWS SDK for PHP](https://docs.aws.amazon.com/AmazonS3/latest/dev/RetrieveObjSingleOpPHP.html) guide.

onelinerhub: [How do I use PHP to get an object from an AWS S3 bucket?](https://onelinerhub.com/php-aws/how-do-i-use-php-to-get-an-object-from-an-aws-s--bucket)