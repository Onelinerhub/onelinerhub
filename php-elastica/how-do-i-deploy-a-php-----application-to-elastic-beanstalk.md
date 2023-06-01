# How do I deploy a PHP 7.4 application to Elastic Beanstalk?
// plain

1. Create an Elastic Beanstalk application and environment.
2. Create a `.ebextensions` folder in the root of your project.
3. Create `.config` files in the `.ebextensions` folder to configure the environment and install packages.
4. Create a `Dockerfile` in the root of your project.
5. Build and push the Docker image to Elastic Beanstalk.
6. Create a `.zip` file of your project and upload it to the Elastic Beanstalk environment.
7. Monitor the deployment process and check the application logs.

Example `.config` file:

```
packages:
  yum:
    php74: []
```

Example `Dockerfile`:

```
FROM amazon/aws-eb-php:7.4-apache

COPY . /var/www/html

RUN chown -R www-data:www-data /var/www/html

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
```

## Helpful links
- [Deploying a PHP Application on AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_PHP.html)
- [.ebextensions Configuration Files](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html)
- [Dockerizing a PHP Application](https://docs.docker.com/develop/develop-images/dockerizing-applications/dockerize-php-app/)

onelinerhub: [How do I deploy a PHP 7.4 application to Elastic Beanstalk?](https://onelinerhub.com/php-elastica/how-do-i-deploy-a-php-----application-to-elastic-beanstalk)