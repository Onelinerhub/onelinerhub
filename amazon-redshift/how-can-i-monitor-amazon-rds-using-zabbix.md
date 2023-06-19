# How can I monitor Amazon RDS using Zabbix?
// plain

To monitor Amazon RDS using Zabbix, you need to install Zabbix Agent on the Amazon RDS instance. After the installation is complete, you can configure the Zabbix Agent to collect the required metrics from the Amazon RDS instance.

You can do this by adding the following code block to the Zabbix Agent configuration file (zabbix_agentd.conf):

```
UserParameter=rds.status[*],aws rds describe-db-instances --query 'DBInstances[*].{Status:DBInstanceStatus}' --output text
```

This code block will enable the Zabbix Agent to collect the status of the Amazon RDS instance.

The code block consists of the following parts:

* `UserParameter`: This is a keyword used to define a custom parameter for the Zabbix Agent.

* `rds.status[*]`: This is the name of the parameter.

* `aws rds describe-db-instances --query 'DBInstances[*].{Status:DBInstanceStatus}' --output text`: This is the command that the Zabbix Agent will execute to collect the status of the Amazon RDS instance.

Once the configuration is complete, the Zabbix Agent will start collecting the status of the Amazon RDS instance.

For more information, please refer to the following links:

* [Zabbix Agent](https://www.zabbix.com/documentation/current/manual/appendix/config/zabbix_agentd)
* [Amazon RDS Command Line Reference](https://docs.aws.amazon.com/cli/latest/reference/rds/index.html)

onelinerhub: [How can I monitor Amazon RDS using Zabbix?](https://onelinerhub.com/amazon-redshift/how-can-i-monitor-amazon-rds-using-zabbix)