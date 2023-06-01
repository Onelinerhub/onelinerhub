# How do I set up a PHP application on AWS using MySQL?
// plain

1. Create an EC2 instance:
   - Go to the EC2 dashboard in the AWS Management Console
   - Select “Launch Instance”
   - Select an Amazon Machine Image (AMI) with pre-installed PHP and MySQL
   - Configure the instance type and other settings
   - Create a new security group and open port 80 for web traffic
   - Launch the instance

2. Connect to the instance:
   - Connect to the instance via SSH
   - Install Apache web server
   ```
   sudo apt-get install apache2
   ```

3. Install PHP and MySQL:
   - Install PHP and MySQL
   ```
   sudo apt-get install php7.0 libapache2-mod-php7.0 php7.0-mysql
   ```

4. Configure MySQL:
   - Create a new database
   ```
   CREATE DATABASE my_database;
   ```
   - Create a new user
   ```
   CREATE USER 'my_user'@'localhost' IDENTIFIED BY 'my_password';
   ```
   - Grant privileges to the user
   ```
   GRANT ALL ON my_database.* TO 'my_user'@'localhost';
   ```

5. Upload your PHP application:
   - Upload your application files to the instance
   - Configure Apache to serve the application

6. Visit your application:
   - Visit your application URL in a web browser

7. Monitor your application:
   - Monitor the performance of your application using CloudWatch

Relevant Links
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/index.html)
- [Deploy a PHP Application on Amazon Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html)

onelinerhub: [How do I set up a PHP application on AWS using MySQL?](https://onelinerhub.com/php-aws/how-do-i-set-up-a-php-application-on-aws-using-mysql)