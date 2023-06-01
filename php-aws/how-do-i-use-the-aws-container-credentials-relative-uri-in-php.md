# How do I use the AWS container credentials relative URI in PHP?
// plain

To use the AWS container credentials relative URI in PHP, you will need to use the Amazon S3 PHP SDK. The SDK allows you to access and manage objects in Amazon S3 using the credentials relative URI.

Here is an example code snippet that shows how to use the credentials relative URI:
```
<?php

// Include the AWS SDK
require 'aws-autoloader.php';

// Create an S3 client
$s3Client = new Aws\S3\S3Client([
    'region' => 'us-west-2',
    'version' => 'latest'
]);

// Get the object from S3 using the credentials relative URI
$result = $s3Client->getObject([
    'Bucket' => 'my-bucket',
    'Key' => 'my-object',
    '@credentials' => 'relative-uri://my-credentials'
]);

// Print the body of the object
echo $result['Body'];

```

The output of the code above will be the body of the object that was retrieved from S3.

## Code explanation

1. Require the AWS SDK - This includes the SDK into the script so that the S3 client can be created.
2. Create an S3 client - This creates a new S3 client using the specified region and version.
3. Get the object from S3 using the credentials relative URI - This retrieves the object from S3 using the credentials relative URI.
4. Print the body of the object - This prints the body of the object that was retrieved.

## Helpful links
- [Amazon S3 PHP SDK](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)
- [Using Credentials Relative URIs](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_relative_uris.html)

onelinerhub: [How do I use the AWS container credentials relative URI in PHP?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-container-credentials-relative-uri-in-php)