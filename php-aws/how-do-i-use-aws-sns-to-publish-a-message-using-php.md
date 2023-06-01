# How do I use AWS SNS to publish a message using PHP?
// plain

To use AWS SNS to publish a message using PHP, you must first install the AWS SDK for PHP. You can then use the following code to publish a message:

```php
<?php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

// Create an SNS client
$sns = new Aws\Sns\SnsClient([
    'region'  => 'us-east-1',
    'version' => 'latest'
]);

// Publish a message to an SNS topic
$result = $sns->publish([
    'Message' => 'Hello world!',
    'TopicArn' => 'arn:aws:sns:us-east-1:123456789012:MyTopic',
]);

echo $result['MessageId'];
```

This code will produce an output of the `MessageId` of the published message.

## Code explanation

1. `require 'vendor/autoload.php';`: This line includes the AWS SDK for PHP.
2. `$sns = new Aws\Sns\SnsClient([...])`: This line creates an SNS client.
3. `$result = $sns->publish([...])`: This line publishes a message to an SNS topic.
4. `echo $result['MessageId'];`: This line prints out the `MessageId` of the published message.

For more information, please refer to the following links:
- [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/installation.html)
- [Publish to an Amazon SNS Topic](https://docs.aws.amazon.com/sns/latest/dg/sns-publish-to-topic.html)

onelinerhub: [How do I use AWS SNS to publish a message using PHP?](https://onelinerhub.com/php-aws/how-do-i-use-aws-sns-to-publish-a-message-using-php)