# How to install TCPDF on Ubuntu using PHP?
// plain

1. **Download TCPDF**
   Download the latest version of TCPDF from [this link](https://tcpdf.org/download).
2. **Unzip the file**
   Unzip the `tcpdf.zip` file to a directory of your choice.
3. **Configure TCPDF**
   Open the `config/tcpdf_config.php` file and configure the `K_PATH_MAIN` constant to the absolute path to the TCPDF library.
4. **Include TCPDF in your project**
   Add the following code to your project to include TCPDF:
   ```php
   require_once('/path/to/tcpdf/tcpdf.php');
   ```
5. **Create a new TCPDF object**
   Create a new TCPDF object with the following code:
   ```php
   $pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
   ```
6. **Generate PDF**
   Generate the PDF by adding the following code:
   ```php
   $pdf->AddPage();
   $pdf->Write(0, 'Hello World!');
   $pdf->Output('example.pdf', 'I');
   ```
7. **Output**
   The code will generate a PDF file with the content "Hello World!".

onelinerhub: [How to install TCPDF on Ubuntu using PHP?](https://onelinerhub.com/php-tcpdf/how-to-install-tcpdf-on-ubuntu-using-php)