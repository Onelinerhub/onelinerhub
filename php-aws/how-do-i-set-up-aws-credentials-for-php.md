# How do I set up AWS credentials for PHP?
// plain

In order to set up AWS credentials for PHP, you'll need to have an AWS account and an API key.

To begin, you'll need to install the AWS SDK for PHP, which can be done via Composer:
```
composer require aws/aws-sdk-php
```

Then, you'll need to set up your credentials. You can do this by creating an AWS credentials file at `~/.aws/credentials` containing your API key and secret key. The file should look like this:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

Next, you'll need to configure the SDK. You can do this by creating an AWS configuration file at `~/.aws/config` containing your region. The file should look like this:
```
[default]
region=us-east-1
```

Finally, you'll need to set up the credentials in your PHP code. This can be done by setting the credentials in the AWS SDK for PHP client:
```php
$sharedConfig = [
    'region'  => 'us-east-1',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'YOUR_ACCESS_KEY_ID',
        'secret' => 'YOUR_SECRET_ACCESS_KEY',
    ],
];

$sdk = new Aws\Sdk($sharedConfig);
```

Once all of these steps are complete, you should have your AWS credentials set up for PHP.

## Code explanation
**

1. `composer require aws/aws-sdk-php` - This command will install the AWS SDK for PHP.
2. `[default]` - This is used to indicate the default profile to use when accessing AWS services.
3. `aws_access_key_id = YOUR_ACCESS_KEY_ID` - This is the access key ID associated with your AWS account.
4. `aws_secret_access_key = YOUR_SECRET_ACCESS_KEY` - This is the secret key associated with your AWS account.
5. `region=us-east-1` - This is the AWS region that you want to use.
6. `$sdk = new Aws\Sdk($sharedConfig);` - This line of code will create a new instance of the AWS SDK for PHP, using the configuration stored in the `$sharedConfig` array.

**## Helpful links**

- [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/basic-usage.html)
- [AWS Credentials File](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

onelinerhub: [How do I set up AWS credentials for PHP?](https://onelinerhub.com/php-aws/how-do-i-set-up-aws-credentials-for-php)