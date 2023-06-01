# How can I use PHP to retrieve an object from AWS?
// plain

You can use the AWS SDK for PHP to retrieve an object from AWS. To do this, you must first [install the SDK](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_installation.html) and configure it with your AWS credentials.

Once the SDK is installed, you can use the following code to retrieve an object from an S3 bucket:

```php
// Include the SDK
require 'vendor/autoload.php';

// Create an S3 client
$s3Client = new Aws\S3\S3Client([
    'region' => 'us-east-1',
    'version' => 'latest'
]);

// Retrieve the object
$result = $s3Client->getObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-object.txt',
]);

// Print the object
echo $result['Body'];
```

This code will print the contents of the `my-object.txt` file from the `my-bucket` S3 bucket.

The code consists of the following parts:

1. `require 'vendor/autoload.php'`: This line includes the AWS SDK for PHP.
2. `$s3Client = new Aws\S3\S3Client([ ... ])`: This line creates an S3 client object.
3. `$result = $s3Client->getObject([ ... ])`: This line retrieves the object from the S3 bucket.
4. `echo $result['Body']`: This line prints the contents of the object.

For more information, see the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started.html).

onelinerhub: [How can I use PHP to retrieve an object from AWS?](https://onelinerhub.com/php-aws/how-can-i-use-php-to-retrieve-an-object-from-aws)