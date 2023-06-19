# How do I use Express.js to upload a file to Amazon S3?
// plain

The following example demonstrates how to use Express.js to upload a file to Amazon S3.

```javascript
// require the AWS SDK
const AWS = require('aws-sdk');

// configure the keys for accessing AWS
AWS.config.update({
    accessKeyId: 'ACCESS_KEY_ID',
    secretAccessKey: 'SECRET_ACCESS_KEY'
});

// create an instance of S3
const s3 = new AWS.S3();

// define the bucket and file name
const bucketName = 'BUCKET_NAME';
const fileName = 'FILE_NAME';

// read content from the file
const fileContent = fs.readFileSync(fileName);

// set up the parameters for upload
const uploadParams = {
    Bucket: bucketName,
    Key: fileName,
    Body: fileContent
};

// upload the file to S3
s3.upload(uploadParams, function (err, data) {
    if (err) {
        console.log('Error', err);
    }
    if (data) {
        console.log('Uploaded in:', data.Location);
    }
});
```

## Output example
 `Uploaded in: <S3_Location>`

1. Require the AWS SDK - `const AWS = require('aws-sdk');`
2. Configure the keys for accessing AWS - `AWS.config.update({ accessKeyId: 'ACCESS_KEY_ID', secretAccessKey: 'SECRET_ACCESS_KEY' });`
3. Create an instance of S3 - `const s3 = new AWS.S3();`
4. Define the bucket and file name - `const bucketName = 'BUCKET_NAME'; const fileName = 'FILE_NAME';`
5. Read content from the file - `const fileContent = fs.readFileSync(fileName);`
6. Set up the parameters for upload - `const uploadParams = { Bucket: bucketName, Key: fileName, Body: fileContent };`
7. Upload the file to S3 - `s3.upload(uploadParams, function (err, data) { ... });`

## Helpful links
- [AWS SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/welcome.html)
- [Uploading Objects Using the AWS SDK for JavaScript](https://docs.aws.amazon.com/AmazonS3/latest/dev/UploadObjSingleOpJS.html)

onelinerhub: [How do I use Express.js to upload a file to Amazon S3?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-upload-a-file-to-amazon-s-)