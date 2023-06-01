# How do I deploy a PHP application to Elastic Beanstalk?
// plain

1. Create a zip archive of your PHP application.
2. Log in to the AWS Management Console and open the Elastic Beanstalk console.
3. Create a new application or select an existing one.
4. Create a new environment or select an existing one.
5. Select the web server environment type.
6. Select the PHP platform and upload the zip archive.
7. Click Create Environment to deploy the application.

## Example code

```
zip -r myapp.zip myapp
```
## Output example

```
adding: myapp/ (stored 0%)
adding: myapp/index.php (deflated 42%)
adding: myapp/style.css (deflated 52%)
```

## Code explanation

- `zip -r myapp.zip myapp`: This command creates a zip archive of your PHP application.
- `adding: myapp/ (stored 0%)`: This indicates that the directory structure is stored in the zip archive.
- `adding: myapp/index.php (deflated 42%)`: This indicates that the index.php file is compressed in the zip archive.
- `adding: myapp/style.css (deflated 52%)`: This indicates that the style.css file is compressed in the zip archive.

## Helpful links
- [AWS Elastic Beanstalk Documentation](https://aws.amazon.com/documentation/elastic-beanstalk/)
- [Deploying a PHP Application on AWS Elastic Beanstalk](https://aws.amazon.com/getting-started/tutorials/deploy-php-application-elastic-beanstalk/)

onelinerhub: [How do I deploy a PHP application to Elastic Beanstalk?](https://onelinerhub.com/php-elastica/how-do-i-deploy-a-php-application-to-elastic-beanstalk)