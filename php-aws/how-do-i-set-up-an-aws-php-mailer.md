# How do I set up an AWS PHP mailer?
// plain

1. First, install the AWS SDK for PHP using Composer by running the following command:
```
composer require aws/aws-sdk-php
```

2. Next, create an SES client object and pass your AWS credentials to it:
```
$sesClient = new \Aws\Ses\SesClient([
    'version'     => 'latest',
    'region'      => 'us-east-1',
    'credentials' => [
        'key'    => 'your_aws_key',
        'secret' => 'your_aws_secret',
    ],
]);
```

3. Then, create the message body with the desired parameters:
```
$messageBody = [
    'Source' => 'sender@example.com',
    'Destination' => [
        'ToAddresses' => [
            'recipient@example.com',
        ],
    ],
    'Message' => [
        'Subject' => [
            'Data' => 'Test Email',
            'Charset' => 'utf-8',
        ],
        'Body' => [
            'Text' => [
                'Data' => 'This is a test email sent from AWS SES.',
                'Charset' => 'utf-8',
            ],
        ],
    ],
];
```

4. Finally, send the email using the SES client's `sendEmail` method:
```
$result = $sesClient->sendEmail($messageBody);
```

This will return an object with the `MessageId` of the sent email.

5. To verify that your email has been sent, you can use the `getSendQuota` method to view your current sending limits and the `getSendStatistics` method to view your sending activity:
```
$quota = $sesClient->getSendQuota();
$stats = $sesClient->getSendStatistics();
```

6. To complete the setup, you must also [verify your email address](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html) and [set up the necessary DNS records](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/dns-records.html) in order for SES to send emails from your domain.

7. You can find more information and examples on using the AWS SDK for PHP to send emails with SES in the [official documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-php.html).

onelinerhub: [How do I set up an AWS PHP mailer?](https://onelinerhub.com/php-aws/how-do-i-set-up-an-aws-php-mailer)