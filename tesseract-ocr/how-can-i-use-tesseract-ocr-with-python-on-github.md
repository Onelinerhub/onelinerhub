# How can I use Tesseract OCR with Python on GitHub?
// plain

Tesseract OCR can be used with Python on GitHub by using the `pytesseract` library. This library provides an easy-to-use wrapper for the Tesseract OCR engine.

## Example code

```python
import pytesseract
import cv2

# Read image
img = cv2.imread("sample.jpg")

# Apply OCR
text = pytesseract.image_to_string(img)

# Print recognized text
print(text)
```

## Output example

```
This is a sample text
```

## Code explanation

- `import pytesseract`: Imports the pytesseract library.
- `import cv2`: Imports the OpenCV library.
- `img = cv2.imread("sample.jpg")`: Reads the image from the file `sample.jpg`.
- `text = pytesseract.image_to_string(img)`: Applies OCR to the image and stores the recognized text in the `text` variable.
- `print(text)`: Prints the recognized text.

## Helpful links
- [pytesseract Documentation](https://pypi.org/project/pytesseract/)
- [Tesseract OCR on GitHub](https://github.com/tesseract-ocr/tesseract)

onelinerhub: [How can I use Tesseract OCR with Python on GitHub?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-with-python-on-github)