# How can I debug my PHP application using Elastic Beanstalk?
// plain

Debugging your PHP application using Elastic Beanstalk is a simple process.

1. Firstly, you need to enable logging for your application. This can be done by adding the following code to your .ebextensions/01_logging.config file:

```
option_settings:
  - namespace: aws:elasticbeanstalk:application:environment
    option_name: LOG_FILE_LOG_LEVEL
    value: DEBUG
```

2. You can also enable logging for Apache and PHP by adding the following code to your .ebextensions/01_logging.config file:

```
files:
  "/etc/httpd/conf.d/php_logging.conf":
    mode: "000644"
    owner: root
    group: root
    content: |
      LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
      LogFormat "%{X-Forwarded-For}i %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" proxy
      SetEnvIf Request_URI "^/php-status$" dontlog
      SetEnvIf Request_URI "^/server-status$" dontlog
      CustomLog /var/log/httpd/php_access.log combined env=!dontlog
```

3. After adding the code, you need to deploy your application. You can do this by running the following command:

```
eb deploy
```

4. Once your application is deployed, you can view the logs by running the following command:

```
eb logs
```

5. You can also view the logs in the AWS Management Console by navigating to the Elastic Beanstalk tab, selecting your application and then clicking on the Logs tab.

This should help you debug your PHP application using Elastic Beanstalk.

## Helpful links
- [AWS Documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-gettingstarted.html)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/elastic-beanstalk)

onelinerhub: [How can I debug my PHP application using Elastic Beanstalk?](https://onelinerhub.com/php-elastica/how-can-i-debug-my-php-application-using-elastic-beanstalk)