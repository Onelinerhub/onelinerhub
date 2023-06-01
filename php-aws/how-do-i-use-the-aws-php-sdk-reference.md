# How do I use the AWS PHP SDK reference?
// plain

The AWS PHP SDK reference provides a comprehensive guide to using the AWS SDK for PHP. To use the reference, you'll first need to install the SDK. The easiest way to do this is to use Composer:

```
composer require aws/aws-sdk-php
```

Once the SDK is installed, you can use the reference to learn how to work with the different services provided by AWS. For example, to create an S3 client:

```
$s3 = new Aws\S3\S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);
```

The code above creates a new S3 client, using the latest version of the SDK and the us-east-1 region. You can then use the client to list buckets:

```
$buckets = $s3->listBuckets();

foreach ($buckets['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

The code above will list the buckets in the S3 account.

The AWS PHP SDK reference also includes code snippets for working with other services, such as EC2, SNS, and DynamoDB. It also provides detailed information about the different classes and methods available in the SDK.

## Helpful links

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [AWS PHP SDK Reference](https://docs.aws.amazon.com/aws-sdk-php/v3/api/)

onelinerhub: [How do I use the AWS PHP SDK reference?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-php-sdk-reference)