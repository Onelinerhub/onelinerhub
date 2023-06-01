# How do I access the PHP error log in an Elastic Beanstalk environment?
// plain

The PHP error log in an Elastic Beanstalk environment can be accessed in several ways.

1. You can access the error log from the Elastic Beanstalk console. Go to the environment page, and select the Logs link. This will open a page containing all the logs associated with the environment. The PHP error log will be listed as `/var/log/httpd/error_log`.

2. You can also access the error log from the command line. SSH into the environment's instance, and run the following command:

```
$ sudo tail -f /var/log/httpd/error_log
```

This will output the contents of the error log in real time.

3. You can also enable access to the error log via the Elastic Beanstalk console. Go to the environment page, and select the Configuration link. Select the Software Configuration option, and under the Log Options section, check the box labeled `Enable log file rotation`. Once the log rotation is enabled, the error log will be available from the Logs page.

## Helpful links

- [Elastic Beanstalk Logs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.loggingS3.html)
- [Tailing Logs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.loggingTail.html)

onelinerhub: [How do I access the PHP error log in an Elastic Beanstalk environment?](https://onelinerhub.com/php-elastica/how-do-i-access-the-php-error-log-in-an-elastic-beanstalk-environment)