# How can I connect to Amazon Web Services (AWS) S3 using PHP?
// plain

To connect to Amazon Web Services (AWS) S3 using PHP, the following steps can be followed:

1. Install the AWS SDK for PHP using Composer:
```
composer require aws/aws-sdk-php
```

2. Create an IAM user with the appropriate access rights to access the S3 buckets.

3. Create an AWS access key and secret access key for the user.

4. Configure the AWS SDK for PHP with the access key and secret access key:
```
$s3 = new Aws\S3\S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1',
    'credentials' => [
        'key'    => 'AKIAIOSFODNN7EXAMPLE',
        'secret' => 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    ],
]);
```

5. Use the SDK to access the S3 buckets:
```
$result = $s3->listBuckets();

// Each Bucket is represented by a KeyValuePair object
foreach ($result['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

6. Output:
```
my-bucket
my-other-bucket
```

7. For more information, please refer to the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/).

onelinerhub: [How can I connect to Amazon Web Services (AWS) S3 using PHP?](https://onelinerhub.com/php-aws/how-can-i-connect-to-amazon-web-services--aws--s--using-php)