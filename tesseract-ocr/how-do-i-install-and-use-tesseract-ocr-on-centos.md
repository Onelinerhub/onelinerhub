# How do I install and use Tesseract OCR on CentOS?
// plain

1. Install Tesseract OCR on CentOS by using the following command:
```
yum install tesseract
```
2. After installation is complete, you can use Tesseract OCR through the command line. To do this, you need to specify the language you want to use. For example, to use English, use the following command:
```
tesseract input_image.png output_text -l eng
```
3. You can also use Tesseract OCR through the Python library PyTesseract. To do this, you need to install the library first by using the following command:
```
pip install pytesseract
```
4. After installation is complete, you can use the library by importing it into your code. An example code would look like this:
```
import pytesseract
from PIL import Image

img = Image.open('input_image.png')
text = pytesseract.image_to_string(img, lang="eng")
print(text)
```
5. The code above will read the input image and output the recognized text in English.

6. You can find more information about Tesseract OCR on CentOS in the following links:
- [Tesseract OCR Documentation](https://tesseract-ocr.github.io/tessdoc/Home.html)
- [Installing Tesseract on CentOS](https://computingforgeeks.com/how-to-install-tesseract-on-centos-8/)
- [Using PyTesseract Library](https://pypi.org/project/pytesseract/)

onelinerhub: [How do I install and use Tesseract OCR on CentOS?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-and-use-tesseract-ocr-on-centos)