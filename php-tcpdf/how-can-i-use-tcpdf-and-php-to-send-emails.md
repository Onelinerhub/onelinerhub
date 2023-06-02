# How can I use TCPDF and PHP to send emails?
// plain

You can use TCPDF and PHP to send emails by creating a PDF document and then attaching it to an email. The following example code creates a basic PDF document and attaches it to an email:

```
<?php
// Include the TCPDF library
require_once('tcpdf_include.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Your Name');
$pdf->SetTitle('My PDF Document');
$pdf->SetSubject('My PDF Document');

// add a page
$pdf->AddPage();

// set font
$pdf->SetFont('helvetica', '', 12);

// output the HTML content
$pdf->writeHTML('<h1>My PDF Document</h1>', true, false, true, false, '');

//Close and output PDF document
$pdf->Output('my_pdf_document.pdf', 'I');

// email stuff (change data below)
$to = "you@example.com";
$from = "me@example.com";
$subject = "My PDF Document";
$message = "<p>Please see the attachment.</p>";

// a random hash will be necessary to send mixed content
$separator = md5(time());

// carriage return type (we use a PHP end of line constant)
$eol = PHP_EOL;

// attachment name
$filename = "my_pdf_document.pdf";

// encode data (puts attachment in proper format)
$pdfdoc = $pdf->Output("", "S");
$attachment = chunk_split(base64_encode($pdfdoc));

// main header
$headers  = "From: ".$from.$eol;
$headers .= "MIME-Version: 1.0".$eol;
$headers .= "Content-Type: multipart/mixed; boundary=\"".$separator."\"";

// no more headers after this, we start the body! //

$body = "--".$separator.$eol;
$body .= "Content-Transfer-Encoding: 7bit".$eol.$eol;
$body .= "".$message."".$eol;

// message
$body .= "--".$separator.$eol;
$body .= "Content-Type: text/html; charset=\"iso-8859-1\"".$eol;
$body .= "Content-Transfer-Encoding: 8bit".$eol.$eol;
$body .= $message.$eol;

// attachment
$body .= "--".$separator.$eol;
$body .= "Content-Type: application/octet-stream; name=\"".$filename."\"".$eol;
$body .= "Content-Transfer-Encoding: base64".$eol;
$body .= "Content-Disposition: attachment".$eol.$eol;
$body .= $attachment.$eol;
$body .= "--".$separator."--";

// send message
mail($to, $subject, $body, $headers);

?>
```

This code will attach the PDF document to an email and send it to the specified address.

The code consists of several parts:

1. **Including the TCPDF library**: The first step is to include the TCPDF library in the code. This is done with the `require_once` statement.

2. **Creating a PDF document**: The next step is to create a PDF document. This is done with the `$pdf = new TCPDF()` statement.

3. **Setting document information**: The document information can be set with the `SetCreator()`, `SetAuthor()`, `SetTitle()` and `SetSubject()` methods.

4. **Adding a page**: The `AddPage()` method is used to add a page to the document.

5. **Writing HTML content**: The `writeHTML()` method is used to write HTML content to the document.

6. **Outputting the PDF document**: The `Output()` method is used to output the PDF document.

7. **Creating the email**: The `mail()` function is used to create the email and attach the PDF document to it.

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs.php)
- [PHP mail() Function](https://www.php.net/manual/en/function.mail.php)

onelinerhub: [How can I use TCPDF and PHP to send emails?](https://onelinerhub.com/php-tcpdf/how-can-i-use-tcpdf-and-php-to-send-emails)