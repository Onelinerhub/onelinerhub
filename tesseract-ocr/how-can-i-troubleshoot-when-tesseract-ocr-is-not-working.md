# How can I troubleshoot when Tesseract OCR is not working?
// plain

Troubleshooting Tesseract OCR can be a complex process, but there are some steps you can take to help identify and fix any issues you may be having.

1. Verify that your image is clean and free of noise. Tesseract OCR works best with images that are clear and free of any distortions.

2. Make sure you have the latest version of Tesseract installed. You can check the version of Tesseract you have installed by running the following command:
```
tesseract --version
```
## Output example

```
tesseract 5.0.0-alpha.20200328
```

3. If you are using a language file, make sure it is installed correctly and that you are specifying the correct language when running Tesseract. You can check the language files installed on your system with the following command:
```
tesseract --list-langs
```
## Output example

```
List of available languages (4):
eng
osd
spa
hin
```

4. If you are still having problems, try running Tesseract with the `--psm` flag set to a different value. This flag can be used to specify the page segmentation mode, which can help Tesseract better identify the text in your image.

5. Make sure you are providing Tesseract with the correct image file type. Tesseract can only read certain types of image files, such as .tiff and .png.

6. If you are still having problems, try using the `--oem` flag to specify the OCR engine mode. This flag can be used to select a different engine mode, which can help Tesseract better identify the text in your image.

7. If you are still having problems, you may want to check out the Tesseract OCR documentation or search online for solutions to your problem.

## Helpful links
- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract/wiki)
- [Troubleshooting Tesseract OCR](https://www.makeuseof.com/tag/troubleshooting-tesseract-ocr/)

onelinerhub: [How can I troubleshoot when Tesseract OCR is not working?](https://onelinerhub.com/tesseract-ocr/how-can-i-troubleshoot-when-tesseract-ocr-is-not-working)