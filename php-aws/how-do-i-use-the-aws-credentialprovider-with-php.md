# How do I use the AWS CredentialProvider with PHP?
// plain

The AWS CredentialProvider is a library that allows developers to easily access AWS credentials from within their PHP applications. This is done by providing a single interface that can be used to access credentials from a variety of sources, such as environment variables, AWS IAM roles, and the AWS SDK for PHP.

To use the AWS CredentialProvider with PHP, you first need to install the library using composer:

```
composer require aws/aws-sdk-php-credentials
```

Once installed, you can use the CredentialProvider to access credentials from a variety of sources. For example, to access credentials from an environment variable, you could use the following code:

```
$credentials = new Aws\Credentials\CredentialProvider();
$credentials = $credentials->env();
```

The `env()` method will look for credentials in environment variables, such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. If found, it will return an `Aws\Credentials\CredentialsInterface` object containing the credentials.

You can also use the CredentialProvider to access credentials from an AWS IAM role. To do this, you can use the `assumeRole()` method, which takes an `Aws\Sts\StsClient` object and an IAM role to assume:

```
$sts = new Aws\Sts\StsClient([
    'region' => 'us-east-1',
    'version' => 'latest'
]);

$credentials = new Aws\Credentials\CredentialProvider();
$credentials = $credentials->assumeRole($sts, 'arn:aws:iam::123456789012:role/MyRole');
```

The `assumeRole()` method will return an `Aws\Credentials\CredentialsInterface` object containing the credentials for the assumed IAM role.

You can find more information about the AWS CredentialProvider in the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/guide/credentials.html).

onelinerhub: [How do I use the AWS CredentialProvider with PHP?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-credentialprovider-with-php)