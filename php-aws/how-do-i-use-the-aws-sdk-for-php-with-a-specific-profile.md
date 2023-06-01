# How do I use the AWS SDK for PHP with a specific profile?
// plain

The AWS SDK for PHP can be used with a specific profile by using the `set_profile()` method. This method takes the profile name as an argument. For example:

```php
$client = new Aws\S3\S3Client([
    'profile' => 'my_profile',
]);
```

The profile name is then used to look up the appropriate credentials in the [shared credentials file](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_profiles.html).

Alternatively, you can also pass the credentials directly when creating the client:

```php
$client = new Aws\S3\S3Client([
    'credentials' => [
        'key'    => 'my_key',
        'secret' => 'my_secret',
    ],
]);
```

The credentials can also be passed as an [AWS credentials provider](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_providers.html).

For more information on using profiles with the AWS SDK for PHP, see the [official documentation](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_profiles.html).

onelinerhub: [How do I use the AWS SDK for PHP with a specific profile?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-sdk-for-php-with-a-specific-profile)