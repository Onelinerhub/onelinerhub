# How do I use the PHP AWS SDK to create an example application?
// plain

The [PHP AWS SDK](https://docs.aws.amazon.com/aws-sdk-php/v3/api/index.html) provides a set of libraries for interacting with the AWS services. To create an example application with the SDK, you can use the following steps:

1. Install the AWS SDK for PHP using [Composer](https://getcomposer.org/):
```
composer require aws/aws-sdk-php
```

2. Create a file `example.php` and include the autoloader:
```php
<?php
require 'vendor/autoload.php';
```

3. Initialize the SDK with your [credentials](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html):
```php
$credentials = new Aws\Credentials\Credentials('<aws access key>', '<aws secret key>');
$sdk = new Aws\Sdk([
    'region'   => 'us-east-1',
    'version'  => 'latest',
    'credentials' => $credentials
]);
```

4. Use the SDK to access an AWS service, for example [S3](https://aws.amazon.com/s3/):
```php
$s3 = $sdk->createS3();
$result = $s3->listBuckets();

foreach ($result['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

5. Run the example application:
```
php example.php
```

6. Output:
```
my-first-bucket
my-second-bucket
```

For more information on using the AWS SDK for PHP, see the [official documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/index.html).

onelinerhub: [How do I use the PHP AWS SDK to create an example application?](https://onelinerhub.com/php-aws/how-do-i-use-the-php-aws-sdk-to-create-an-example-application)