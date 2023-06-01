# How to deploy PHP on AWS?
// plain

Deploying PHP on AWS can be done in the following steps:

1. Create an AWS account.
2. Launch an EC2 instance.
3. Connect to your instance using SSH.
4. Install Apache web server and PHP with the following command:
```
sudo yum install -y httpd24 php56
```
5. Configure the web server and PHP, for example, by editing the `/etc/php.ini` file.
6. Create a web page with a `.php` extension and put it in the document root folder (e.g. `/var/www/html`).
7. Access the web page from your browser.

## Helpful links
- [Getting Started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [Installing Apache Web Server and PHP on Amazon Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html)

onelinerhub: [How to deploy PHP on AWS?](https://onelinerhub.com/php-aws/how-to-deploy-php-on-aws)