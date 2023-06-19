# How do I install Tesseract OCR on Windows?
// plain

1. Download the Tesseract OCR Installer from [here](https://github.com/UB-Mannheim/tesseract/wiki).
2. Run the executable file to start the installation process.
3. Make sure to select the language you want to use.
4. After installation, add the Tesseract executable path to the system environment variables. To do this, open the Control Panel > System > Advanced System Settings > Environment Variables and add the Tesseract executable path to the Path variable.
5. To check if the installation was successful, open the command prompt and type `tesseract --version`. This should output the version of Tesseract installed.
6. To test the Tesseract OCR, create a test image file with some text and save it in a folder.
7. To extract the text from the image, open the command prompt and type `tesseract <image_name.extension> <output_file_name>`. This should create a text file with the extracted text.

```
tesseract test.jpg output
```

## Output example


```
Tesseract Open Source OCR Engine v5.0.0-alpha.20200328 with Leptonica
```

onelinerhub: [How do I install Tesseract OCR on Windows?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-tesseract-ocr-on-windows-1687148463)