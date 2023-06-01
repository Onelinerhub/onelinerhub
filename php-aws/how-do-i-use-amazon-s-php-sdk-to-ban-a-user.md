# How do I use Amazon's PHP SDK to ban a user?
// plain

Using Amazon's PHP SDK to ban a user requires the following steps:

1. Include the Amazon PHP SDK library in your project:
```
require 'vendor/autoload.php';
```

2. Create an Amazon Cognito Identity client. This is used to access the Amazon Cognito user pool:
```
$cognitoClient = new CognitoIdentityClient([
    'region' => 'us-east-1',
    'version' => '2016-04-18',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ],
]);
```

3. Get the user pool ID and the user pool client ID from the AWS console:
```
$userPoolId = 'YOUR_USER_POOL_ID';
$clientId = 'YOUR_CLIENT_ID';
```

4. Create an Amazon Cognito user pool client:
```
$userPoolClient = new CognitoUserPool($cognitoClient, $userPoolId, $clientId);
```

5. Get the user to ban:
```
$userToBan = $userPoolClient->getUser('USERNAME');
```

6. Ban the user:
```
$userToBan->adminDisableUser();
```

7. Check if the user has been successfully banned:
```
if ($userToBan->isEnabled()) {
    echo 'User is not banned.';
} else {
    echo 'User is banned.';
}
```

## Output example

```
User is banned.
```

## Helpful links

- [Amazon Cognito Documentation](https://docs.aws.amazon.com/cognito/index.html)
- [Amazon Cognito Identity Client](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.CognitoIdentity.CognitoIdentityClient.html)
- [Amazon Cognito User Pool Client](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.CognitoIdentityProvider.CognitoUserPool.html)

onelinerhub: [How do I use Amazon's PHP SDK to ban a user?](https://onelinerhub.com/php-aws/how-do-i-use-amazon-s-php-sdk-to-ban-a-user)