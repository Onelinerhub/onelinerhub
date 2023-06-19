# How do I download the Amazon Redshift JDBC driver?
// plain

1. Go to the [Amazon Redshift JDBC Driver Download page](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html#download-jdbc-driver).
2. Click the link for the latest version of the driver.
3. Save the file to your computer.
4. Unzip the driver file.
5. You should find a file named `RedshiftJDBC42-no-awssdk.jar`.
6. To add the driver to your CLASSPATH, add the following line to your `.bash_profile`:
```
export CLASSPATH=$CLASSPATH:/path/to/RedshiftJDBC42-no-awssdk.jar
```
7. After adding the line to your `.bash_profile`, run the following command to apply the change:
```
source ~/.bash_profile
```

* `RedshiftJDBC42-no-awssdk.jar`: The driver file for Amazon Redshift
* `.bash_profile`: A file that contains environment settings for your shell
* `CLASSPATH`: An environment variable that tells the Java Virtual Machine where to look for class files
* `source`: A command that reads and executes commands from a file

onelinerhub: [How do I download the Amazon Redshift JDBC driver?](https://onelinerhub.com/amazon-redshift/how-do-i-download-the-amazon-redshift-jdbc-driver)