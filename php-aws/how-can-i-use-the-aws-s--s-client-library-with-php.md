# How can I use the AWS S3 S3Client library with PHP?
// plain

Using the AWS S3 S3Client library with PHP is relatively straightforward. Here is an example of code that can be used to list the objects in a bucket:

```php
<?php
require 'vendor/autoload.php';

use Aws\S3\S3Client;

$s3 = new S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);

$objects = $s3->listObjects([
    'Bucket' => 'my-bucket'
]);

foreach ($objects['Contents'] as $object) {
    echo $object['Key'] . "\n";
}
?>
```

## Code explanation


1. Require the autoloader: `require 'vendor/autoload.php';`
2. Use the S3Client class: `use Aws\S3\S3Client;`
3. Create a new S3Client instance: `$s3 = new S3Client([`
4. Set the version and region: `'version' => 'latest', 'region'  => 'us-east-1'`
5. List the objects in the bucket: `$objects = $s3->listObjects([ 'Bucket' => 'my-bucket' ]);`
6. Iterate over the results and output the object keys:
```
foreach ($objects['Contents'] as $object) {
    echo $object['Key'] . "\n";
}
```

## Helpful links

- [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/basic-usage.html)
- [S3Client Class](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)

onelinerhub: [How can I use the AWS S3 S3Client library with PHP?](https://onelinerhub.com/php-aws/how-can-i-use-the-aws-s--s-client-library-with-php)