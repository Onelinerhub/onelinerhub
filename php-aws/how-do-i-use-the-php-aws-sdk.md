# How do I use the PHP AWS SDK?
// plain

The [PHP AWS SDK](https://aws.amazon.com/sdk-for-php/) is a set of libraries, code samples, and documentation for developers to build applications and services on Amazon Web Services.

Using the PHP AWS SDK is fairly straightforward. First, you need to install the SDK using [Composer](https://getcomposer.org/):

```
$ composer require aws/aws-sdk-php
```

Once the SDK is installed, you can create an `Aws\Sdk` object which acts as an entry point to the AWS services. You will need to provide credentials and a region to the constructor:

```php
$sdk = new Aws\Sdk([
    'region'   => 'us-east-1',
    'version'  => 'latest',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ],
]);
```

Once you have the `$sdk` object, you can create client objects for each AWS service you want to use. For example, to create an Amazon S3 client:

```php
$s3 = $sdk->createS3();
```

You can then use the client object to make API calls. For example, to list all the buckets in your account:

```php
$result = $s3->listBuckets();

foreach ($result['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

For more information, see the [PHP AWS SDK documentation](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started.html).

onelinerhub: [How do I use the PHP AWS SDK?](https://onelinerhub.com/php-aws/how-do-i-use-the-php-aws-sdk)