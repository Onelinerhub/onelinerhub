# How do I change the PHP version using Elastic Beanstalk?
// plain

Using Elastic Beanstalk, you can easily change the version of PHP that your application is running on.

1. First, you will need to create a configuration file in the .ebextensions folder of your application. This file should be named something like `01_change_php_version.config` and should contain the following code:

```
files:
  "/etc/httpd/conf.d/php.conf":
    mode: "000644"
    owner: root
    group: root
    content: |
      <FilesMatch \.php$>
        SetHandler application/x-httpd-php71
      </FilesMatch>

container_commands:
  01_change_php_version:
    command: "rm -f /etc/httpd/conf.d/php.conf"
```

2. This configuration file will replace the existing `php.conf` file with one that sets the PHP version to `php71`. This can be changed to any other version of PHP that is supported by Elastic Beanstalk.

3. Once the configuration file has been created, you can deploy your application to Elastic Beanstalk. The configuration file will be picked up and applied during the deployment process, and your application will now be running on the new version of PHP.

## Helpful links
- [Elastic Beanstalk Configuration Files](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html)
- [PHP Versions Supported by Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html#concepts.platforms.php)

onelinerhub: [How do I change the PHP version using Elastic Beanstalk?](https://onelinerhub.com/php-elastica/how-do-i-change-the-php-version-using-elastic-beanstalk)