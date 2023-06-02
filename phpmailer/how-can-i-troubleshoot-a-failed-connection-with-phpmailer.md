# How can I troubleshoot a failed connection with PHPMailer?
// plain

1. Check for syntax errors in your code - use a linter such as [PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) to check for any syntax errors.

2. Check your authentication credentials - make sure the username and password you are using to authenticate with PHPMailer are correct.

3. Check the SMTP server settings - ensure that the SMTP server settings are correct and that the SMTP server is reachable from your server.

4. Check for any firewall or network issues - if the SMTP server is not reachable, check for any firewall or network issues that may be blocking the connection.

5. Test the connection with telnet - use telnet to test the connection to the SMTP server. For example:

```
telnet smtp.example.com 25
```

6. Check the log files - check the log files for any errors that may be related to the connection.

7. Check the PHPMailer documentation - consult the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Troubleshooting) for additional troubleshooting tips and solutions.

onelinerhub: [How can I troubleshoot a failed connection with PHPMailer?](https://onelinerhub.com/phpmailer/how-can-i-troubleshoot-a-failed-connection-with-phpmailer)