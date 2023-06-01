# How do I use the PHP AWS S3 PutObject command?
// plain

The PHP AWS S3 PutObject command is used to upload an object to an Amazon S3 bucket. To use it, you need to have the AWS SDK for PHP library installed and configured.

To use the PutObject command, you need to create an instance of the S3Client class and pass it the credentials of the AWS account. You can then call the PutObject method on the S3Client instance, passing in the bucket name, object name, and the file contents.

## Example code

```
// Include the AWS SDK for PHP library
require '/path/to/aws-autoloader.php';

// Create an S3Client instance with your AWS credentials
$s3 = new S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ],
]);

// Upload an object to the specified bucket
$result = $s3->putObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-object.txt',
    'Body'   => 'This is the data for my object',
]);
```

The parts of the code are:

1. Include the AWS SDK for PHP library: This line includes the AWS SDK for PHP library, which is needed to use the PutObject command.

2. Create an S3Client instance: This line creates an S3Client instance, passing it the credentials of the AWS account.

3. Call the PutObject method: This line calls the PutObject method on the S3Client instance, passing in the bucket name, object name, and the file contents.

The output of the code will be an object containing information about the uploaded object, such as its ETag and version ID.

## Helpful links

- [AWS SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_installation.html)
- [S3Client class](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)
- [PutObject method](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putobject)

onelinerhub: [How do I use the PHP AWS S3 PutObject command?](https://onelinerhub.com/php-aws/how-do-i-use-the-php-aws-s--putobject-command)