# How do I configure the path for a PHP application on AWS Elastic Beanstalk?
// plain

1. Create an `.ebextensions` folder in the root of your application directory.
2. Create a `.config` file in the `.ebextensions` folder.
3. Add the following code to the `.config` file to configure the path for your PHP application:

```
files:
  "/etc/httpd/conf.d/php.conf":
    mode: "000644"
    owner: root
    group: root
    content: |
      <Directory "/var/app/current/public">
        AllowOverride All
        Require all granted
        php_admin_value include_path "/var/app/current/lib:/usr/share/pear"
      </Directory>
```

4. Zip up the application and deploy it to Elastic Beanstalk.
5. After the application is deployed, the `php.conf` file will be created in the `/etc/httpd/conf.d` folder.
6. This will configure the path for your PHP application.
7. You can view the path configuration in the `php.conf` file.

## Helpful links
- [AWS Elastic Beanstalk Documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [Configuring an Apache Web Server](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions-apache.html)

onelinerhub: [How do I configure the path for a PHP application on AWS Elastic Beanstalk?](https://onelinerhub.com/php-elastica/how-do-i-configure-the-path-for-a-php-application-on-aws-elastic-beanstalk)