# How can I add a digital signature to a PDF using PHP and TCPDF?
// plain

To add a digital signature to a PDF using PHP and TCPDF, you can use the TCPDF library's `setSignature()` method. This method takes four parameters: the signature data, the name of the signature, the location of the signature, and the appearance of the signature. Here is an example code block that shows how to use this method:

```
<?php
    // Include the TCPDF library
    require_once('tcpdf.php');

    // Create a new TCPDF object
    $pdf = new TCPDF();

    // Set the signature data
    $signatureData = '...';

    // Set the signature name
    $signatureName = 'My Signature';

    // Set the signature location
    $signatureLocation = 'My City';

    // Set the signature appearance
    $signatureAppearance = '...';

    // Add the signature to the PDF
    $pdf->setSignature($signatureData, $signatureName, $signatureLocation, $signatureAppearance);

?>
```

## Code explanation

- `require_once('tcpdf.php');`: This line includes the TCPDF library.
- `$pdf = new TCPDF();`: This line creates a new TCPDF object.
- `$signatureData = '...';`: This line sets the signature data.
- `$signatureName = 'My Signature';`: This line sets the signature name.
- `$signatureLocation = 'My City';`: This line sets the signature location.
- `$signatureAppearance = '...';`: This line sets the signature appearance.
- `$pdf->setSignature($signatureData, $signatureName, $signatureLocation, $signatureAppearance);`: This line adds the signature to the PDF.

## Helpful links
- [TCPDF Library](https://tcpdf.org/)
- [setSignature() Method Documentation](https://tcpdf.org/doc/classTCPDF/#a7d8d3f1f9a3d5f04c3c7d7d7f3a85b2f)

onelinerhub: [How can I add a digital signature to a PDF using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-add-a-digital-signature-to-a-pdf-using-php-and-tcpdf)