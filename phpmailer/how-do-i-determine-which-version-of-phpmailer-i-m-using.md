# How do I determine which version of PHPMailer I'm using?
// plain

To determine which version of PHPMailer you are using, you can access the `version` property of the PHPMailer class.

## Example code

```
require 'PHPMailer/PHPMailerAutoload.php';
$mail = new PHPMailer;
echo $mail->version;
```

## Output example

```
6.1.7
```

The above code will output the version of PHPMailer that is currently being used.

Alternatively, you can look at the `CHANGELOG.md` file provided in the PHPMailer repository. This file contains a list of changes and updates made to the PHPMailer library, including the version number for each release.

## Helpful links
- [PHPMailer repository](https://github.com/PHPMailer/PHPMailer/)
- [CHANGELOG.md](https://github.com/PHPMailer/PHPMailer/blob/master/CHANGELOG.md)

onelinerhub: [How do I determine which version of PHPMailer I'm using?](https://onelinerhub.com/phpmailer/how-do-i-determine-which-version-of-phpmailer-i-m-using)