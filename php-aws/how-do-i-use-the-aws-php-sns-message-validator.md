# How do I use the AWS PHP SNS Message Validator?
// plain

The AWS PHP SNS Message Validator is a library that can be used to validate messages sent to an Amazon SNS topic.

To use the AWS PHP SNS Message Validator, first install the library using Composer:

```
composer require aws/aws-php-sns-message-validator
```

Once the library is installed, you can use it to validate SNS messages. For example:

```
$message = json_decode($snsMessage);
$validator = new \Aws\Sns\MessageValidator();
$validator->validate($message);
```

The code above will decode the SNS message from JSON and then use the MessageValidator class to validate the message. If the validation is successful, the code will not throw any exceptions.

The MessageValidator class also provides methods for retrieving the message attributes and the message body. For example:

```
$attributes = $validator->getAttributes();
$body = $validator->getBody();
```

The MessageValidator class also provides methods for verifying the message signature and the message type. For example:

```
$validator->isValid();
$validator->isType('Notification');
```

For more information on using the AWS PHP SNS Message Validator, see the [official documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Sns.MessageValidator.html).

onelinerhub: [How do I use the AWS PHP SNS Message Validator?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-php-sns-message-validator)