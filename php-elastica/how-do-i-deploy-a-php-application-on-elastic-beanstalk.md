# How do I deploy a PHP application on Elastic Beanstalk?
// plain

1. Create an Elastic Beanstalk application using the AWS Management Console.
2. Create an Elastic Beanstalk environment within the application.
3. Upload your PHP application code to the environment. This can be done using the AWS Management Console, AWS CLI, or the AWS SDK.
4. Create a configuration file, `.ebextensions/php.config`, with the following content:

```
files:
  "/etc/httpd/conf.d/php.conf":
    mode: "000644"
    owner: root
    group: root
    content: |
      <FilesMatch \.php$>
        SetHandler application/x-httpd-php
      </FilesMatch>

packages:
  yum:
    php: []

container_commands:
  00_enable_mod_rewrite:
    command: "sudo ln -s /etc/httpd/mods-available/rewrite.load /etc/httpd/conf.d/rewrite.load"
```

5. Create a `.platform/platform.yml` file with the following content:

```
version: 1

default_region: us-east-1

runtime:
  name: php
  version: 7.4
```

6. Create an Elastic Beanstalk environment.
7. Deploy your application to the environment.

## Helpful links
- [AWS Elastic Beanstalk Documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [PHP on AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-development-environment.html)

onelinerhub: [How do I deploy a PHP application on Elastic Beanstalk?](https://onelinerhub.com/php-elastica/how-do-i-deploy-a-php-application-on-elastic-beanstalk)