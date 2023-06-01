# How can I use the AWS SDK with PHP Composer?
// plain

The AWS SDK for PHP can be used with Composer by adding the SDK as a dependency in your project's `composer.json` file. You can do this by running the following command in the root of your project:

```
composer require aws/aws-sdk-php
```

This will download and install the AWS SDK for PHP and its dependencies into your project's `vendor` directory. You can then use the SDK in your project by including the autoloader in your project's bootstrap file:

```
require 'vendor/autoload.php';
```

Once the autoloader is included, you can make calls to any of the AWS services. For example, to create an Amazon S3 client:

```php
$s3 = new Aws\S3\S3Client([
    'region'  => 'us-east-1',
    'version' => '2006-03-01',
]);
```

You can find more information about using the AWS SDK for PHP with Composer in the [official documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/installation.html#installing-via-composer).

onelinerhub: [How can I use the AWS SDK with PHP Composer?](https://onelinerhub.com/php-aws/how-can-i-use-the-aws-sdk-with-php-composer)