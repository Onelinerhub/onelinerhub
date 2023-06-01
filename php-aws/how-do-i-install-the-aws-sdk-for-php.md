# How do I install the AWS SDK for PHP?
// plain

1. To install the AWS SDK for PHP, you need to have [Composer](https://getcomposer.org/) installed.

2. After Composer is installed, you can run the command `composer require aws/aws-sdk-php` to install the SDK.

3. Once the SDK is installed, you can include it in your project by adding the following line to your code:

```php
require_once 'vendor/autoload.php';
```

4. You can then use the SDK in your project by creating an instance of the [Aws\Sdk](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Sdk.html) class:

```php
$sdk = new Aws\Sdk([
    'region'   => 'us-west-2',
    'version'  => 'latest',
]);
```

5. You can then use the SDK to interact with AWS services, such as creating an [S3 Client](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html):

```php
$s3Client = $sdk->createS3();
```

6. For more information, please refer to the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/).

7. You can also find more examples of how to use the SDK in the [AWS SDK for PHP GitHub repository](https://github.com/aws/aws-sdk-php).

onelinerhub: [How do I install the AWS SDK for PHP?](https://onelinerhub.com/php-aws/how-do-i-install-the-aws-sdk-for-php)