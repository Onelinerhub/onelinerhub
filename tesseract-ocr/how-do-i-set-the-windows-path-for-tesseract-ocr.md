# How do I set the Windows path for Tesseract OCR?
// plain

To set the Windows path for Tesseract OCR, you need to:

1. Open the Windows Control Panel
2. Go to System and Security > System
3. Select Advanced System Settings
4. On the Advanced tab, click the Environment Variables button
5. Under System Variables, select Path and click the Edit button
6. Add the path to the Tesseract OCR folder to the end of the list, for example: `C:\Program Files\Tesseract-OCR`
7. Click OK to save the changes.

You can also use the command line to set the Windows path for Tesseract OCR. For example, to add the path `C:\Program Files\Tesseract-OCR` to the existing path variable, you can use the following command:

```
setx path "%path%;C:\Program Files\Tesseract-OCR"
```

The output of this command should be `SUCCESS: Specified value was saved`.

## Helpful links

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Setting the Windows Path](https://docs.oracle.com/en/database/oracle/r-enterprise/1.5.1/oread/setting-the-windows-path.html)

onelinerhub: [How do I set the Windows path for Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-set-the-windows-path-for-tesseract-ocr)