# How can I deploy a PHP application using Elastic Beanstalk and Amazon RDS?
// plain

1. Create an Amazon Web Services (AWS) account.
2. Create an Amazon RDS instance.
3. Create an Elastic Beanstalk application.
4. Upload your PHP application to the Elastic Beanstalk application.
5. Configure the Elastic Beanstalk application to use the Amazon RDS instance.
6. Deploy the application to the Elastic Beanstalk application.
7. Test the application to make sure it is working properly.

## Example code

```
$ eb create my-php-application
```

## Output example

```
Creating application version archive "app-d4d3-160812_035020".
Uploading my-php-application/app-d4d3-160812_035020.zip to S3.
This may take a while.
Upload Complete.
Environment details for: my-php-application
  Application name: my-php-application
  Region: us-east-1
  Deployed Version: app-d4d3-160812_035020
  Environment ID: e-r2p4qf3fjk
  Platform: arn:aws:elasticbeanstalk:us-east-1::platform/PHP 7.3 running on 64bit Amazon Linux/2.9.5
  Tier: WebServer-Standard-1.0
  CNAME: my-php-application.us-east-1.elasticbeanstalk.com
  Updated: 2020-08-12 03:50:22.827000+00:00
Printing Status:
INFO: createEnvironment is starting.
INFO: Using elasticbeanstalk-us-east-1-123456789 as Amazon S3 storage bucket for environment data.
```

## Code explanation

- `eb create my-php-application`: This command creates an Elastic Beanstalk application with the name my-php-application.

## Helpful links
- [Getting Started with AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)
- [Creating an AWS Elastic Beanstalk Environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-resources.html)
- [Connecting Your Elastic Beanstalk Environment to Amazon RDS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html)

onelinerhub: [How can I deploy a PHP application using Elastic Beanstalk and Amazon RDS?](https://onelinerhub.com/php-elastica/how-can-i-deploy-a-php-application-using-elastic-beanstalk-and-amazon-rds)