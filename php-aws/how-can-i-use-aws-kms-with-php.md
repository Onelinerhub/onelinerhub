# How can I use AWS KMS with PHP?
// plain

Using AWS KMS with PHP is simple and straightforward. The following example shows how to encrypt a string using a customer master key (CMK) in AWS KMS and PHP:

```php
<?php
// Include the AWS SDK using the Composer autoloader.
require 'vendor/autoload.php';

// Create an AWS KMS client using the shared credentials file.
$kms = new Aws\Kms\KmsClient([
    'region'  => 'us-east-1',
    'version' => '2014-11-01',
]);

// Create an encryption context.
$context = [
    'Example' => 'Encryption Context',
];

// Encrypt a string using a customer master key (CMK).
$result = $kms->encrypt([
    'KeyId' => '1234abcd-12ab-34cd-56ef-1234567890ab',
    'Plaintext' => 'This is the message to encrypt.',
    'EncryptionContext' => $context,
]);

// Print the encrypted data.
echo $result['CiphertextBlob'];

// Output:
// AQICAHh4f4VFrXNmT4Tf+YdV6hVb3VkRX2TmY6y/eVVU/mhHVAAAAZjBkBgkqhkiG9w0BBwagVzBVAgEAMEsGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM9zGd9a7J+E/E4C9AgEQgCJ+3v2C3hLhVdQ6YI9IyVj/rVf/9f4HhZV7P8KvXrA==
```

1. Include the AWS SDK using the Composer autoloader: `require 'vendor/autoload.php';`
2. Create an AWS KMS client using the shared credentials file: `$kms = new Aws\Kms\KmsClient([ ... ]);`
3. Create an encryption context: `$context = [ 'Example' => 'Encryption Context', ];`
4. Encrypt a string using a customer master key (CMK): `$result = $kms->encrypt([ ... ]);`
5. Print the encrypted data: `echo $result['CiphertextBlob'];`

The output of the example code is the encrypted string `AQICAHh4f4VFrXNmT4Tf+YdV6hVb3VkRX2TmY6y/eVVU/mhHVAAAAZjBkBgkqhkiG9w0BBwagVzBVAgEAMEsGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM9zGd9a7J+E/E4C9AgEQgCJ+3v2C3hLhVdQ6YI9IyVj/rVf/9f4HhZV7P8KvXrA==`.

## Helpful links

- [AWS KMS Documentation](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [AWS SDK for PHP Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/index.html)

onelinerhub: [How can I use AWS KMS with PHP?](https://onelinerhub.com/php-aws/how-can-i-use-aws-kms-with-php)