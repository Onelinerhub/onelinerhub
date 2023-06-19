# How do I set the path for Tesseract OCR?
// plain

Setting the path for Tesseract OCR is a necessary step in order to use the software.

1. Firstly, you need to download the Tesseract OCR software from [GitHub](https://github.com/tesseract-ocr/tesseract/wiki).
2. Once downloaded, extract the files into a directory, for example `C:\Program Files\Tesseract-OCR`.
3. Next, you need to set the path in the environment variables.

To do this:

1. Go to `Control Panel > System and Security > System > Advanced System Settings > Environment Variables`.
2. Under `System Variables`, look for `Path` and click `Edit`.
3. Add the path of the Tesseract-OCR directory to the end of the `Path` variable. For example:

```
C:\Program Files\Tesseract-OCR;
```

4. Click `OK` to save the changes.

You can verify that the path has been set correctly by opening a command prompt and typing `echo %PATH%`. This should output the path that you have set for Tesseract OCR.

```
C:\Program Files\Tesseract-OCR;
```

onelinerhub: [How do I set the path for Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-set-the-path-for-tesseract-ocr)