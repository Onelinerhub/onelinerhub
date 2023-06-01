# How can I use PHP and AWS Transcribe to transcribe audio files?
// plain

Using PHP and AWS Transcribe, audio files can be transcribed into text. The following example code shows how to use the AWS SDK for PHP to transcribe a file stored in an Amazon S3 bucket:

```
// Include the AWS SDK
require 'vendor/autoload.php';

// Create an AWS Transcribe client
$transcribe = new Aws\TranscribeService\TranscribeServiceClient([
    'region' => 'us-east-1',
    'version' => 'latest'
]);

// Define the Amazon S3 bucket and file to transcribe
$s3_bucket = 'my-audio-files';
$s3_key = 'example-audio-file.mp3';

// Create a transcription job
$transcribe->startTranscriptionJob([
    'LanguageCode' => 'en-US',
    'Media' => [
        'MediaFileUri' => "s3://{$s3_bucket}/{$s3_key}"
    ],
    'MediaFormat' => 'mp3',
    'TranscriptionJobName' => 'example-transcription-job'
]);
```

This code will create an AWS Transcribe job to transcribe the audio file stored in the S3 bucket. Once the job is complete, the transcribed text will be available in the S3 bucket.

The code consists of the following parts:

1. Include the AWS SDK - This line includes the AWS SDK for PHP, which is required to use the AWS Transcribe service.
2. Create an AWS Transcribe client - This line creates a TranscribeServiceClient object, which is used to interact with the AWS Transcribe service.
3. Define the Amazon S3 bucket and file to transcribe - This line defines the name of the S3 bucket and the key of the file to transcribe.
4. Create a transcription job - This line creates a transcription job using the TranscribeServiceClient object. It specifies the language of the audio file, the location of the audio file, the format of the audio file, and the name of the transcription job.

Once the job is complete, the transcribed text will be available in the S3 bucket.

## Helpful links

- [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.TranscribeService.TranscribeServiceClient.html)
- [AWS Transcribe Documentation](https://docs.aws.amazon.com/transcribe/latest/dg/what-is-transcribe.html)

onelinerhub: [How can I use PHP and AWS Transcribe to transcribe audio files?](https://onelinerhub.com/php-aws/how-can-i-use-php-and-aws-transcribe-to-transcribe-audio-files)