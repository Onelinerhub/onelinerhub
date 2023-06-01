# How can I use Amazon Elastic Transcoder with PHP?
// plain

Amazon Elastic Transcoder is a media transcoding service that can be used to convert media files from their original source format into different formats that are optimized for different devices. The service can be used with PHP by using the AWS SDK for PHP.

The following example code will demonstrate how to use the AWS SDK for PHP to create a job in Amazon Elastic Transcoder:

```php
<?php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

use Aws\ElasticTranscoder\ElasticTranscoderClient;

$client = ElasticTranscoderClient::factory(array(
    'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
    'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    'region' => 'us-east-1'
));

$result = $client->createJob(array(
    'Input' => array(
        'Key' => 'input.mp4',
    ),
    'Output' => array(
        'Key' => 'output.mp4',
        'PresetId' => '1351620000001-000010'
    )
));

echo $result['Job']['Id'];
```

This code will output the ID for the newly created job in Amazon Elastic Transcoder.

Parts of the code:

- `require 'vendor/autoload.php'`: Includes the AWS SDK for PHP using the Composer autoloader.
- `use Aws\ElasticTranscoder\ElasticTranscoderClient`: Loads the Elastic Transcoder client.
- `$client = ElasticTranscoderClient::factory(...)`: Creates an Elastic Transcoder client.
- `$result = $client->createJob(...)`: Creates a job in Elastic Transcoder.
- `echo $result['Job']['Id']`: Outputs the ID for the newly created job.

## Helpful links

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [Amazon Elastic Transcoder Documentation](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/introduction.html)

onelinerhub: [How can I use Amazon Elastic Transcoder with PHP?](https://onelinerhub.com/php-elastica/how-can-i-use-amazon-elastic-transcoder-with-php)