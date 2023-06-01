# How do I use the PHP AWS SDK to get an object?
// plain

The PHP AWS SDK provides a client to interact with AWS services. To get an object, use the `getObject()` method of the client. The following example code shows how to use the `getObject()` method to get an object from an S3 bucket:

```php
// Create a client
$client = new Aws\S3\S3Client([
    'region'  => 'us-west-2',
    'version' => 'latest'
]);

// Get an object
$result = $client->getObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-object'
]);

echo $result['Body'];
```

This code will output the contents of the object. The `getObject()` method takes an array as its argument, which must include the `Bucket` and `Key` parameters. The `Bucket` parameter is the name of the bucket which contains the object, and the `Key` parameter is the name of the object.

## Helpful links

- [PHP AWS SDK Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/index.html)
- [AWS S3 GetObject Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getobject)

onelinerhub: [How do I use the PHP AWS SDK to get an object?](https://onelinerhub.com/php-aws/how-do-i-use-the-php-aws-sdk-to-get-an-object)