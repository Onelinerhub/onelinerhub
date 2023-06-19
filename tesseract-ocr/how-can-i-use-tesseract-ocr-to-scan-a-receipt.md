# How can I use Tesseract OCR to scan a receipt?
// plain

Tesseract OCR is an open source optical character recognition (OCR) engine developed by Google. It can be used to scan receipts and extract text from them. The following example code shows how to use Tesseract OCR to scan a receipt:

```
# import the necessary packages
from PIL import Image
import pytesseract

# load the image
image = Image.open("receipt.jpg")

# run tesseract OCR on the image
text = pytesseract.image_to_string(image)

# print the extracted text
print(text)
```

This code will output the extracted text from the receipt. The code consists of the following parts:

1. Import the necessary packages: `from PIL import Image` and `import pytesseract`
2. Load the image: `image = Image.open("receipt.jpg")`
3. Run tesseract OCR on the image: `text = pytesseract.image_to_string(image)`
4. Print the extracted text: `print(text)`

For more information on Tesseract OCR and how to use it to scan receipts, see the following links:

- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract/wiki)
- [How to Extract Text from Images Using Tesseract OCR in Python](https://www.geeksforgeeks.org/extract-text-from-image-using-ocr-in-python/)

onelinerhub: [How can I use Tesseract OCR to scan a receipt?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-to-scan-a-receipt)