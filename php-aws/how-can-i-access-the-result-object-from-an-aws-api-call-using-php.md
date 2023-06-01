# How can I access the result object from an AWS API call using PHP?
// plain

Using the AWS SDK for PHP, you can access the result object from an AWS API call. The following example code will demonstrate this:

```php
<?php

// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Instantiate an Amazon S3 client.
$s3 = new Aws\S3\S3Client([
    'version'     => 'latest',
    'region'      => 'us-east-1',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ]
]);

// Call the Amazon S3 API
$result = $s3->listBuckets();

// Access the result object
echo $result['Buckets'][0]['Name'];

// Outputs: example-bucket
```

The code above:

1. Includes the SDK using the Composer autoloader.
2. Instantiates an Amazon S3 client.
3. Calls the Amazon S3 API.
4. Accesses the result object and prints the name of the first bucket.

The output of the code is:

```
example-bucket
```

For more information, see the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/index.html).

onelinerhub: [How can I access the result object from an AWS API call using PHP?](https://onelinerhub.com/php-aws/how-can-i-access-the-result-object-from-an-aws-api-call-using-php)