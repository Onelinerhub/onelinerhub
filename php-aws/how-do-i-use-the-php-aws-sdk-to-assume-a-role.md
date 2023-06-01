# How do I use the PHP AWS SDK to assume a role?
// plain

The PHP AWS SDK provides a convenient way to assume a role using the `assumeRole` method.

```php
// Create a client using the default credential profile
$stsClient = new Aws\Sts\StsClient([
    'region' => 'us-east-1',
    'version' => 'latest'
]);

// Get the assumed role credentials
$result = $stsClient->assumeRole([
    'RoleArn' => 'arn:aws:iam::123456789012:role/example-role',
    'RoleSessionName' => 'example-session',
]);

// Extract the assumed role credentials
$credentials = $result->get('Credentials');
```
The above code will return an array containing the assumed role credentials.

The `assumeRole` method takes two parameters:
1. `RoleArn` - The Amazon Resource Name (ARN) of the role to assume.
2. `RoleSessionName` - An identifier for the assumed role session.

The `assumeRole` method returns an array containing the following credentials:
1. `AccessKeyId` - The access key for the assumed role.
2. `SecretAccessKey` - The secret access key for the assumed role.
3. `SessionToken` - The session token for the assumed role.
4. `Expiration` - The expiration time for the assumed role credentials.

## Helpful links
- [AWS SDK for PHP Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Sts.StsClient.html#_assumeRole)
- [AssumeRole API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

onelinerhub: [How do I use the PHP AWS SDK to assume a role?](https://onelinerhub.com/php-aws/how-do-i-use-the-php-aws-sdk-to-assume-a-role)