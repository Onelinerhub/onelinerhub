# How do I upload a file to AWS S3 using PHP?
// plain

The following example code shows how to upload a file to an AWS S3 bucket using PHP.

```
<?php
// Include the file containing your AWS access keys
require 'aws-credentials.php';

// Create an S3 client
$s3 = new Aws\S3\S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1',
    'credentials' => [
        'key'    => $aws_access_key_id,
        'secret' => $aws_secret_access_key,
    ]
]);

// Upload a file
$result = $s3->putObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-file.txt',
    'Body'   => 'this is the body!'
]);

// Print the result
echo $result['ObjectURL'];
```

This code will output the URL of the uploaded file, for example: `https://my-bucket.s3.amazonaws.com/my-file.txt`.

The code consists of the following parts:

1. `require 'aws-credentials.php'` - This line includes the file containing your AWS access keys.
2. `$s3 = new Aws\S3\S3Client([])` - This line creates an S3 client object.
3. `$result = $s3->putObject([])` - This line uploads the file to the specified S3 bucket.
4. `echo $result['ObjectURL']` - This line prints the URL of the uploaded file.

For more information, please refer to the [AWS documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/basic-usage.html#uploading-a-file).

onelinerhub: [How do I upload a file to AWS S3 using PHP?](https://onelinerhub.com/php-aws/how-do-i-upload-a-file-to-aws-s--using-php)