# How do I deploy a PHP application to AWS?
// plain

1. Create an Amazon EC2 instance, preferably with an Amazon Machine Image (AMI) that is tailored for running PHP applications.
2. Connect to the instance using SSH or the Amazon EC2 console.
3. Upload your application files to the instance using SFTP, SCP or the Amazon EC2 console.
4. Install any necessary software packages and libraries required for your application.
5. Configure your web server to serve the application files.
6. Configure the security groups to allow access to the application.
7. Test the application to ensure that it works as expected.

Example code block:
```
$ sudo yum install httpd php
$ sudo service httpd start
```
Output of example code:
```
Starting httpd:                                            [  OK  ]
```
## Code explanation

- `sudo yum install httpd php`: Installs the Apache web server and the PHP language interpreter.
- `sudo service httpd start`: Starts the Apache web server.

## Helpful links
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [Amazon Machine Image (AMI)](https://aws.amazon.com/amazon-linux-ami/)
- [Secure Shell (SSH)](https://en.wikipedia.org/wiki/Secure_Shell)
- [File Transfer Protocol (FTP)](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [Secure Copy Protocol (SCP)](https://en.wikipedia.org/wiki/Secure_copy)

onelinerhub: [How do I deploy a PHP application to AWS?](https://onelinerhub.com/php-aws/how-do-i-deploy-a-php-application-to-aws)