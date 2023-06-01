# How can I use Amazon SES to send emails with PHP?
// plain

Using Amazon SES to send emails with PHP is a simple process. First, you'll need to [install and configure the AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/installation.html), then you can use the following code to send an email:

```php
<?php
// Include the AWS SDK using the Composer autoloader.
require 'vendor/autoload.php';

use Aws\Ses\SesClient;

// Create a SesClient
$client = new SesClient([
    'version' => 'latest',
    'region'  => 'us-east-1',
]);

// Send an email
$result = $client->sendEmail([
    'Destination' => [
        'ToAddresses' => [
            'RECIPIENT_EMAIL_ADDRESS',
        ],
    ],
    'Message' => [
        'Body' => [
            'Text' => [
                'Data' => 'Email body',
            ],
        ],
        'Subject' => [
            'Data' => 'Email Subject',
        ],
    ],
    'Source' => 'SENDER_EMAIL_ADDRESS',
]);

echo $result->get('MessageId');
```

The output of this code should be the message ID of the sent email.

This code consists of the following parts:
- `require 'vendor/autoload.php';` - loads the AWS SDK for PHP using the Composer autoloader.
- `use Aws\Ses\SesClient;` - imports the SesClient class from the AWS SDK for PHP.
- `$client = new SesClient([...])` - creates a new SesClient instance.
- `$result = $client->sendEmail([...])` - sends an email using the SesClient instance.
- `echo $result->get('MessageId');` - prints the message ID of the sent email.

For more information about sending emails with Amazon SES, please refer to the [Amazon SES documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-php.html).

onelinerhub: [How can I use Amazon SES to send emails with PHP?](https://onelinerhub.com/php-aws/how-can-i-use-amazon-ses-to-send-emails-with-php)