# How do I deploy a PHP application on Amazon's Elastic Beanstalk?
// plain

1. Set up an AWS account if you don't already have one.
2. Create an Elastic Beanstalk application.
3. Upload your PHP application source code to your Elastic Beanstalk application.
4. Configure the environment for the application.
   ```
   aws elasticbeanstalk create-environment --application-name myApp --environment-name myEnv --solution-stack-name "64bit Amazon Linux 2018.03 v2.9.1 running PHP 7.2"
   ```
5. Deploy the application.
   ```
   aws elasticbeanstalk deploy --application-name myApp --environment-name myEnv --version-label v1 --source mySourceBundle.zip
   ```
   Output:
   ```
   {
       "ApplicationName": "myApp",
       "EnvironmentName": "myEnv",
       "VersionLabel": "v1",
       "DeploymentId": "d-1234567890"
   }
   ```
6. Monitor the application's health.
7. Access the application.

## Helpful links
- [AWS Documentation - Create an Elastic Beanstalk Environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Creating_an_Environment.html)
- [AWS Documentation - Deploying Applications to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-sourcebundle.html)

onelinerhub: [How do I deploy a PHP application on Amazon's Elastic Beanstalk?](https://onelinerhub.com/php-elastica/how-do-i-deploy-a-php-application-on-amazon-s-elastic-beanstalk)