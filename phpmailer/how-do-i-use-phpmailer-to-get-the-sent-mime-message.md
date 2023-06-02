# How do I use PHPMailer to get the sent MIME message?
// plain

Using PHPMailer to get the sent MIME message is easy. The following example code will show you how to do it:

```
<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Load Composer's autoloader
require 'vendor/autoload.php';

// Instantiation and passing `true` enables exceptions
$mail = new PHPMailer(true);

// Get the MIME message
$mime_message = $mail->getSentMIMEMessage();

echo $mime_message;

```

## Output example

```
MIME-Version: 1.0
Date: Sun, 11 Aug 2019 15:06:54 -0700
Message-ID: <5d4f876a7b0a6@example.com>
Subject: Test
From: John Doe <john@example.com>
To: Jane Doe <jane@example.com>
Content-Type: multipart/alternative;
	boundary="b1_9d1a3e0f1b9f8c9a1b4f8c9f2a9c1f7a"

--b1_9d1a3e0f1b9f8c9a1b4f8c9f2a9c1f7a
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit

Hello World!

--b1_9d1a3e0f1b9f8c9a1b4f8c9f2a9c1f7a
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: 8bit

<p>Hello World!</p>

--b1_9d1a3e0f1b9f8c9a1b4f8c9f2a9c1f7a--

```

The code above uses the `$mail->getSentMIMEMessage()` method to get the sent MIME message. This method returns the MIME message as a string, which is then printed out with `echo`.

The MIME message contains the following parts:

- `MIME-Version`: The version of the MIME protocol
- `Date`: The date when the message was sent
- `Message-ID`: A unique identifier for the message
- `Subject`: The subject of the message
- `From`: The sender of the message
- `To`: The recipient of the message
- `Content-Type`: The content type of the message
- `Content-Transfer-Encoding`: The encoding used for the message

For more information on using PHPMailer to get the sent MIME message, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial).

onelinerhub: [How do I use PHPMailer to get the sent MIME message?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-get-the-sent-mime-message)