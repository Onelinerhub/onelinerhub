# How can I troubleshoot PHP TCPDF errors?
// plain

The best way to troubleshoot PHP TCPDF errors is to look at the error log. This will give you a detailed description of the error and help you pinpoint the exact cause. Additionally, you can also try to debug the code by using the following steps:

1. Check the parameters used in the code. Make sure that the parameters are valid and that they are in the correct format.

2. Check the code for any typos or syntax errors.

3. Check for any missing files or libraries.

4. Make sure that the TCPDF library is correctly installed and configured.

5. Check the permissions of the files and folders.

6. Check the server configuration for any possible issues.

7. Test the code in a different environment.

```
// Example code
$pdf = new TCPDF();
$pdf->AddPage();
$pdf->WriteHTML('Hello World!');
$pdf->Output('example.pdf', 'D');
```

## Output example


example.pdf file is generated.

onelinerhub: [How can I troubleshoot PHP TCPDF errors?](https://onelinerhub.com/php-tcpdf/how-can-i-troubleshoot-php-tcpdf-errors)