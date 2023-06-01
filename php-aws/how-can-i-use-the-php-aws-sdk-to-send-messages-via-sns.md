# How can I use the PHP AWS SDK to send messages via SNS?
// plain

The PHP AWS SDK can be used to send messages via SNS (Simple Notification Service). To do this, you will need to set up an AWS account and install the SDK.

Once the SDK is installed, you can use the following code to send a message via SNS:

```
<?php
$sns = new Aws\Sns\SnsClient([
    'region'  => 'us-east-1',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'your-access-key',
        'secret' => 'your-secret-key',
    ],
]);

$result = $sns->publish([
    'Message' => 'Hello World',
    'TopicArn' => 'arn:aws:sns:us-east-1:123456789012:MyTopic',
]);

echo $result['MessageId'];
```

The output of the above code will be the Message ID of the message sent via SNS.

The code can be broken down into the following parts:

1. Initialization of the SNS client. This includes setting the region, version, and credentials.
2. Publish a message to SNS, which includes the message and topic ARN.
3. Output the Message ID of the message sent.

For more information on using the PHP AWS SDK with SNS, please refer to the following link:
https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sns-examples-sending-messages.html

onelinerhub: [How can I use the PHP AWS SDK to send messages via SNS?](https://onelinerhub.com/php-aws/how-can-i-use-the-php-aws-sdk-to-send-messages-via-sns)