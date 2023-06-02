# How do I use TCPDF with PHP to create examples?
// plain

Using TCPDF with PHP to create examples is quite simple. First, you need to include the TCPDF library in your project. This can be done by adding the following line of code to the top of your PHP file:
```php
require_once('tcpdf/tcpdf.php');
```
Next, you need to create an instance of the TCPDF class. This can be done by adding the following line of code:
```php
$pdf = new TCPDF();
```
You can then begin adding content to your PDF document. This can be done by using the `AddPage()` and `WriteHTML()` methods. For example, the following code will create a basic PDF document with a heading and some text:
```php
$pdf->AddPage();
$pdf->WriteHTML('<h1>My PDF Document</h1><p>This is some text in my PDF document.</p>');
```
Finally, you can output the PDF document to the browser or save it to a file by using the `Output()` method. For example, the following code will save the PDF document to a file called `my_document.pdf`:
```php
$pdf->Output('my_document.pdf', 'F');
```

## Code explanation

- `require_once('tcpdf/tcpdf.php');` - include the TCPDF library
- `$pdf = new TCPDF();` - create an instance of the TCPDF class
- `$pdf->AddPage();` - add a new page to the PDF document
- `$pdf->WriteHTML('<h1>My PDF Document</h1><p>This is some text in my PDF document.</p>');` - add content to the PDF document
- `$pdf->Output('my_document.pdf', 'F');` - save the PDF document to a file

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/index.php)

onelinerhub: [How do I use TCPDF with PHP to create examples?](https://onelinerhub.com/php-tcpdf/how-do-i-use-tcpdf-with-php-to-create-examples)