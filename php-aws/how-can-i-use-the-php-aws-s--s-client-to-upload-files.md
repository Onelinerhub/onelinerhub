# How can I use the PHP AWS S3 S3Client to upload files?
// plain

The AWS S3Client in PHP can be used to upload files to an Amazon S3 bucket. The following example code can be used to upload a file:

```
<?php
$s3Client = new Aws\S3\S3Client([
    'region'  => 'us-west-2',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ]
]);

$result = $s3Client->putObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-file.txt',
    'Body'   => 'this is the body!'
]);

echo $result['ObjectURL'];
?>
```

The code above will upload a file named `my-file.txt` to the bucket `my-bucket` with the body `this is the body!`. The `$s3Client` variable is an instance of the S3Client class. The `putObject` method is used to upload the file, and the `ObjectURL` of the uploaded file is returned in the `$result` variable.

## Code explanation


1. `$s3Client`: An instance of the S3Client class.
2. `putObject`: The method used to upload the file.
3. `Bucket`: The name of the bucket to upload the file to.
4. `Key`: The name of the file to be uploaded.
5. `Body`: The body of the file to be uploaded.
6. `$result`: The variable that holds the result of the `putObject` method.
7. `ObjectURL`: The URL of the uploaded file.

## Helpful links

- [AWS S3Client Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)
- [Uploading Objects Using the AWS SDK for PHP](https://docs.aws.amazon.com/AmazonS3/latest/dev/UploadObjSingleOpPHP.html)

onelinerhub: [How can I use the PHP AWS S3 S3Client to upload files?](https://onelinerhub.com/php-aws/how-can-i-use-the-php-aws-s--s-client-to-upload-files)