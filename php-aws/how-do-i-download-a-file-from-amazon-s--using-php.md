# How do I download a file from Amazon S3 using PHP?
// plain

To download a file from Amazon S3 using PHP, the following steps should be taken:
1. Create an Amazon S3 client using your AWS credentials.
```php
$s3Client = new S3Client([
    'version'     => 'latest',
    'region'      => 'us-east-1',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ],
]);
```
2. Set the bucket and the file name from which you would like to download the file.
```php
$bucket = 'my-bucket';
$key    = 'my-file.txt';
```
3. Use the `getObject()` method of the S3Client to download the file.
```php
$result = $s3Client->getObject([
    'Bucket' => $bucket,
    'Key'    => $key
]);
```
4. Use the `saveAs()` method of the `$result` object to save the file to your local file system.
```php
$result->saveAs('/path/to/file.txt');
```

The above code will download the file `my-file.txt` from the `my-bucket` bucket and save it to the `/path/to/file.txt` path in your local file system.

## Helpful links
- [Amazon S3 Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html)
- [S3Client::getObject()](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getobject)
- [Result::saveAs()](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.Result.html#_saveAs)

onelinerhub: [How do I download a file from Amazon S3 using PHP?](https://onelinerhub.com/php-aws/how-do-i-download-a-file-from-amazon-s--using-php)