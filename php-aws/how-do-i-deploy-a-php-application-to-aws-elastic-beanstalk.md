# How do I deploy a PHP application to AWS Elastic Beanstalk?
// plain

1. Create an AWS account and sign in to the AWS Management Console.
2. Create an Elastic Beanstalk application.
3. Create an Elastic Beanstalk environment.
4. Upload the PHP application to the environment.
   ```
   aws elasticbeanstalk create-application-version --application-name <application-name> --version-label <version-label> --source-bundle S3Bucket=<bucket-name>,S3Key=<key-name>
   ```
   Output:
   ```
   {
      "ApplicationVersion": {
         "ApplicationName": "<application-name>",
         "Description": "",
         "VersionLabel": "<version-label>",
         "SourceBundle": {
            "S3Bucket": "<bucket-name>",
            "S3Key": "<key-name>"
         },
         "DateCreated": <date>,
         "DateUpdated": <date>
      }
   }
   ```
5. Update the Elastic Beanstalk environment to use the new application version.
6. Monitor the deployment and access the application.
7. Troubleshoot any issues (if needed).

## Code explanation
**

1. `aws elasticbeanstalk create-application-version --application-name <application-name> --version-label <version-label> --source-bundle S3Bucket=<bucket-name>,S3Key=<key-name>` - Create an application version for the PHP application with the given application name and version label.

**## Helpful links**

- [Deploying a PHP Application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-deployment.html)
- [AWS Elastic Beanstalk CLI Reference](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)

onelinerhub: [How do I deploy a PHP application to AWS Elastic Beanstalk?](https://onelinerhub.com/php-aws/how-do-i-deploy-a-php-application-to-aws-elastic-beanstalk)