# How do I configure my php.ini file for an Elastic Beanstalk application?
// plain

To configure the php.ini file for an Elastic Beanstalk application, follow the steps below:

1. Log into the Elastic Beanstalk console and select the application you want to configure.

2. Select Configuration from the left navigation menu and then select the Software configuration option.

3. Scroll down to the PHP Configuration section and click the Edit button.

4. In the Configuration Details section, select the PHP configuration file option.

5. From the dropdown menu, select the php.ini file that you want to configure.

6. In the Configuration Options section, add the configuration options that you want to set in the php.ini file.

7. Click the Save button to save the changes and then click the Apply button to apply the changes to the Elastic Beanstalk application.

```
[PHP]
memory_limit = 256M
max_execution_time = 30
```

No output.

## Helpful links

- [Elastic Beanstalk Documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [PHP Configuration Options](https://www.php.net/manual/en/ini.list.php)

onelinerhub: [How do I configure my php.ini file for an Elastic Beanstalk application?](https://onelinerhub.com/php-elastica/how-do-i-configure-my-php-ini-file-for-an-elastic-beanstalk-application)