# How can I use the AWS KMS PHP SDK?
// plain

The AWS KMS PHP SDK can be used to programmatically access AWS Key Management Service (KMS) from within PHP applications.

To use the AWS KMS PHP SDK, first install the AWS SDK for PHP via composer:
```
composer require aws/aws-sdk-php
```

Then, create an AWS KMS client object:
```
<?php
use Aws\Kms\KmsClient;

$kms = new KmsClient([
    'region'  => 'us-east-1',
    'version' => '2014-11-01',
    'profile' => 'default'
]);
```

Once the KMS client object is created, you can use the various methods to access KMS services. For example, to list all the keys in your AWS account:

```
<?php
$result = $kms->listKeys();

foreach ($result['Keys'] as $key) {
    echo $key['KeyId'] . "\n";
}
```

The output of the above code will be a list of all the keys in your AWS account.

You can also use the AWS KMS PHP SDK to encrypt and decrypt data, create and delete keys, and manage key policies. For more information, please refer to the [AWS KMS API Reference](https://docs.aws.amazon.com/kms/latest/APIReference/Welcome.html) and the [AWS KMS PHP SDK Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/guide/kms.html).

onelinerhub: [How can I use the AWS KMS PHP SDK?](https://onelinerhub.com/php-aws/how-can-i-use-the-aws-kms-php-sdk)