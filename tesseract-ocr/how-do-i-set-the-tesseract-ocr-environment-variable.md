# How do I set the Tesseract OCR environment variable?
// plain

The Tesseract OCR environment variable can be set in a few different ways.

1. Using the `export` command in the command line:
```
export TESSDATA_PREFIX=/usr/local/share/tessdata
```
2. Adding the `export` command to the `~/.profile` file:
```
echo 'export TESSDATA_PREFIX=/usr/local/share/tessdata' >> ~/.profile
```

3. Setting the environment variable in the application code:
```
# Python
import os
os.environ["TESSDATA_PREFIX"] = "/usr/local/share/tessdata"

# Java
System.setProperty("TESSDATA_PREFIX", "/usr/local/share/tessdata");
```

The environment variable `TESSDATA_PREFIX` should be set to the path of the Tesseract data files.

## Helpful links
- [Tesseract OCR Environment Variable](https://github.com/tesseract-ocr/tesseract/wiki/EnvironmentVariables)
- [Setting Environment Variables in Python](https://docs.python.org/3/library/os.html#os.environ)
- [Setting Environment Variables in Java](https://docs.oracle.com/javase/7/docs/api/java/lang/System.html#setProperty%28java.lang.String,%20java.lang.String%29)

onelinerhub: [How do I set the Tesseract OCR environment variable?](https://onelinerhub.com/tesseract-ocr/how-do-i-set-the-tesseract-ocr-environment-variable)