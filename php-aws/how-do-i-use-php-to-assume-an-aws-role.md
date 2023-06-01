# How do I use PHP to assume an AWS role?
// plain

Assuming an AWS role from an EC2 instance using PHP is done using the AWS SDK for PHP. The following code example shows how to do this:

```
<?php
require 'vendor/autoload.php';

use Aws\Credentials\CredentialProvider;
use Aws\Sts\StsClient;

$sts = new StsClient([
    'region' => 'us-west-2',
    'version' => 'latest',
    'credentials' => CredentialProvider::instance()
]);

$role_arn = 'arn:aws:iam::123456789012:role/MyRole';

$result = $sts->assumeRole([
    'RoleArn' => $role_arn,
    'RoleSessionName' => 'MySessionName'
]);

$credentials = $result->get('Credentials');

$access_key_id = $credentials['AccessKeyId'];
$secret_access_key = $credentials['SecretAccessKey'];
$session_token = $credentials['SessionToken'];

echo "Access Key Id: {$access_key_id}\n";
echo "Secret Access Key: {$secret_access_key}\n";
echo "Session Token: {$session_token}\n";
```

## Output example


```
Access Key Id: <access_key_id>
Secret Access Key: <secret_access_key>
Session Token: <session_token>
```

In the example code above:

1. The `require` statement includes the AWS SDK for PHP.
2. The `use` statements import the necessary classes.
3. The `$sts` variable creates an instance of the `StsClient` class.
4. The `$role_arn` variable contains the ARN of the role to be assumed.
5. The `$result` variable stores the result of the `assumeRole` call.
6. The `$credentials` variable stores the credentials returned by the `assumeRole` call.
7. The `$access_key_id`, `$secret_access_key`, and `$session_token` variables store the credentials returned by the `assumeRole` call.

## Helpful links

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [AssumeRole - AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

onelinerhub: [How do I use PHP to assume an AWS role?](https://onelinerhub.com/php-aws/how-do-i-use-php-to-assume-an-aws-role)