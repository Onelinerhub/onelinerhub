# How can I troubleshoot XAMPP and PHPMailer if they are not working?
// plain

To troubleshoot XAMPP and PHPMailer, you can follow these steps:
1. Check if the XAMPP server is running. You can do this by running the command `netstat -an | find ":80"` in the command prompt. If you see an active connection on port 80, then the XAMPP server is running.
2. Check if the PHPMailer library is installed. You can do this by running the following code in the terminal:
```
<?php
if (class_exists('PHPMailer')) {
    echo 'PHPMailer is installed!';
} else {
    echo 'PHPMailer is not installed!';
}
```
If you see the output `PHPMailer is installed!`, then the library is installed correctly.
3. Make sure that the correct credentials are set in the `php.ini` file. The `php.ini` file should contain the following credentials:
```
[mail function]
; XAMPP: Comment out this if you want to work with an SMTP Server like Mercury
smtp_port=25

; For Win32 only.
; http://php.net/sendmail-from
sendmail_from = postmaster@localhost

; XAMPP IMPORTANT NOTE (1): If XAMPP is installed in a base directory with spaces (e.g. c:\program filesC:\xampp) fakemail and mailtodisk do not work correctly.
; XAMPP IMPORTANT NOTE (2): In this case please copy the sendmail or mailtodisk folder in your root folder (e.g. C:\sendmail) and use this for sendmail_path.
sendmail_path = "\"C:\xampp\sendmail\sendmail.exe\" -t"
```
4. Check if the SMTP port is open. You can do this by running the command `telnet localhost 25` in the command prompt. If you see a response, then the SMTP port is open.
5. Check if the `php.ini` file is being read correctly. You can do this by running the following code in the terminal:
```
<?php
echo ini_get('sendmail_path');
```
If the output of the code matches the `sendmail_path` set in the `php.ini` file, then the `php.ini` file is being read correctly.
6. Make sure that the PHPMailer code is written correctly. You can check the [official documentation](https://github.com/PHPMailer/PHPMailer/blob/master/examples/smtp.phps) to make sure that your code is written correctly.
7. If all the steps above have been completed and the issue is still not resolved, you can check the [PHPMailer troubleshooting guide](https://github.com/PHPMailer/PHPMailer/wiki/Troubleshooting) for more help.

onelinerhub: [How can I troubleshoot XAMPP and PHPMailer if they are not working?](https://onelinerhub.com/phpmailer/how-can-i-troubleshoot-xampp-and-phpmailer-if-they-are-not-working)