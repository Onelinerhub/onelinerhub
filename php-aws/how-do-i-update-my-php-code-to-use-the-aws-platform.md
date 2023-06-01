# How do I update my PHP code to use the AWS platform?
// plain

Updating your PHP code to use the AWS platform is fairly straightforward. First, you'll need to install the AWS SDK for PHP, which is available [here](https://aws.amazon.com/sdk-for-php/). Once you have the SDK installed, you can begin making API calls to the AWS services.

For example, if you wanted to list the contents of an S3 bucket, you could use the following code:

```php
<?php
require 'vendor/autoload.php';

use Aws\S3\S3Client;

$s3Client = new S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);

$bucketContents = $s3Client->listObjects([
    'Bucket' => 'my-bucket'
]);

print_r($bucketContents);
```

This code would output something like this:

```
Array
(
    [Contents] => Array
        (
            [0] => Array
                (
                    [Key] => file1.txt
                    [LastModified] => 2020-04-20T20:30:00.000Z
                    [ETag] => "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
                    [Size] => 11
                    [StorageClass] => STANDARD
                )
        )
)
```

The code above is just one example of how you can use the AWS SDK for PHP to interact with the AWS platform. You can find more examples [here](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/).

onelinerhub: [How do I update my PHP code to use the AWS platform?](https://onelinerhub.com/php-aws/how-do-i-update-my-php-code-to-use-the-aws-platform)