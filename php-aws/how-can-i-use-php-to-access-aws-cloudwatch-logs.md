# How can I use PHP to access AWS CloudWatch Logs?
// plain

PHP can be used to access AWS CloudWatch Logs using the AWS SDK for PHP. This SDK provides access to all the CloudWatch Logs API operations.

To access CloudWatch Logs, you need to first create an AWS client object and pass in your AWS credentials. You can then use the client object to call the CloudWatch Logs API operations.

For example, to list the log groups in your account, you can use the following code:

```php
<?php
// Include the AWS SDK for PHP
require 'vendor/autoload.php';

// Create an AWS client
$client = new Aws\CloudWatchLogs\CloudWatchLogsClient([
    'region' => 'us-east-1',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ],
]);

// List log groups
$result = $client->describeLogGroups();

// Print out the log group names
foreach ($result['logGroups'] as $logGroup) {
    echo $logGroup['logGroupName'] . "\n";
}
```

The output of this code will be a list of log group names associated with your account:

```
MyLogGroup1
MyLogGroup2
MyLogGroup3
```

The code consists of the following parts:

1. Include the AWS SDK for PHP: `require 'vendor/autoload.php';`
2. Create an AWS client object: `$client = new Aws\CloudWatchLogs\CloudWatchLogsClient([...])`
3. Call the `describeLogGroups()` API operation: `$client->describeLogGroups()`
4. Iterate over the log groups and print out the log group names: `foreach ($result['logGroups'] as $logGroup) { echo $logGroup['logGroupName'] . "\n"; }`

## Helpful links

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [CloudWatch Logs API Reference](https://docs.aws.amazon.com/cli/latest/reference/logs/index.html)

onelinerhub: [How can I use PHP to access AWS CloudWatch Logs?](https://onelinerhub.com/php-aws/how-can-i-use-php-to-access-aws-cloudwatch-logs)