# How can I use Tesseract OCR to extract text from an image?
// plain

Tesseract OCR is an open source Optical Character Recognition (OCR) engine. It can be used to extract text from an image. To use Tesseract OCR to extract text from an image, the following steps need to be followed:

1. Install Tesseract OCR on your computer.
2. Import the PyTesseract module.
```python
import pytesseract
```
3. Provide an image file path to the image_to_string() function.
```python
text = pytesseract.image_to_string('image.jpg')
print(text)
```
## Output example

```
This is some example text
```
4. Set the language of the text in the image, if necessary.
```python
text = pytesseract.image_to_string('image.jpg', lang='eng')
```
5. Set the OCR engine mode, if necessary.
```python
text = pytesseract.image_to_string('image.jpg', lang='eng', oem=1)
```
6. Get the text from the image.
```python
text = pytesseract.image_to_string('image.jpg')
```
7. Print the extracted text.
```python
print(text)
```
## Output example

```
This is some example text
```

## Helpful links

- [PyTesseract Documentation](https://pypi.org/project/pytesseract/)
- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract/wiki)

onelinerhub: [How can I use Tesseract OCR to extract text from an image?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-to-extract-text-from-an-image)