# How do I use the AWS ListObjectsV2 function in PHP?
// plain

The AWS ListObjectsV2 function can be used in PHP to list the contents of a bucket. This function returns an array of objects, which contain information about each object in the bucket.

Below is an example code block that uses the ListObjectsV2 function to list the contents of a bucket:

```
<?php
// Include the AWS SDK using the Composer autoloader.
require 'vendor/autoload.php';

use Aws\S3\S3Client;

// Instantiate the S3 client with your AWS credentials
$s3 = new S3Client([
    'version'     => 'latest',
    'region'      => 'us-east-1',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ],
]);

// List the contents of the bucket
$objects = $s3->listObjectsV2(['Bucket' => 'my-bucket']);

print_r($objects);
```

This code will output an array of objects with information about the contents of the bucket, including the object's name, size, and last modified date.

The code consists of the following parts:

1. Include the AWS SDK using the Composer autoloader: This line includes the AWS SDK using the Composer autoloader, which is necessary for using the AWS SDK in PHP.

2. Instantiate the S3 client with your AWS credentials: This line instantiates an S3 client object, which is used for interacting with S3. You need to provide your AWS credentials in order to use the client.

3. List the contents of the bucket: This line uses the ListObjectsV2 function to list the contents of the bucket. You need to provide the name of the bucket in the function's parameter.

4. Print the array of objects: This line prints the array of objects returned by the ListObjectsV2 function.

For more information about using the AWS SDK for PHP, see the [documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/index.html).

onelinerhub: [How do I use the AWS ListObjectsV2 function in PHP?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-listobjectsv--function-in-php)