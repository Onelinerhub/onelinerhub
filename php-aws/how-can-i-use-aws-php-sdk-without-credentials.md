# How can I use AWS PHP SDK without credentials?
// plain

The AWS PHP SDK can be used without credentials by using the `AnonymousAWSCredentials` class. This can be used to make basic requests to AWS services without the need for any credentials.

Below is an example of how to use the `AnonymousAWSCredentials` class to make a request to the AWS S3 service:

```
// Include the AWS SDK
require 'vendor/autoload.php';

// Create a new anonymous credentials object
$credentials = new Aws\Credentials\AnonymousAWSCredentials();

// Create a new S3 client using the anonymous credentials
$s3Client = new Aws\S3\S3Client([
    'region' => 'us-east-1',
    'version' => 'latest',
    'credentials' => $credentials
]);

// Make a request to the S3 service
$result = $s3Client->listBuckets();

// Output the result
print_r($result);
```

## Output example

```
Array
(
    [Buckets] => Array
        (
            [0] => Array
                (
                    [Name] => my-bucket
                    [CreationDate] => 2020-10-20T12:34:56+00:00
                )
            ...
        )
)
```

The code above consists of the following parts:

1. Include the AWS SDK: `require 'vendor/autoload.php';`
2. Create a new anonymous credentials object: `$credentials = new Aws\Credentials\AnonymousAWSCredentials();`
3. Create a new S3 client using the anonymous credentials:
```
$s3Client = new Aws\S3\S3Client([
    'region' => 'us-east-1',
    'version' => 'latest',
    'credentials' => $credentials
]);
```
4. Make a request to the S3 service: `$result = $s3Client->listBuckets();`
5. Output the result: `print_r($result);`

For more information, please refer to the [AWS PHP SDK Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/guide/credentials.html).

onelinerhub: [How can I use AWS PHP SDK without credentials?](https://onelinerhub.com/php-aws/how-can-i-use-aws-php-sdk-without-credentials)