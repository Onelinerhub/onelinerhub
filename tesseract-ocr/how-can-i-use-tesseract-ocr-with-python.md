# How can I use Tesseract OCR with Python?
// plain

Tesseract OCR is a powerful open source Optical Character Recognition (OCR) engine. It can be used with Python using the pytesseract package. Pytesseract is an optical character recognition (OCR) tool for python. It is also the basis for simple image support in other Python libraries such as SciPy and Matplotlib.

To use Tesseract OCR with Python, follow these steps:

1. Install the pytesseract package: `pip install pytesseract`
2. Import the package: `import pytesseract`
3. Provide a path to the tesseract executable: `pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"`
4. Read the image using OpenCV: `img = cv2.imread("image.jpg")`
5. Run Tesseract OCR on the image: `text = pytesseract.image_to_string(img)`

## Example code

```
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("image.jpg")
text = pytesseract.image_to_string(img)

print(text)
```

## Output example

```
This is a sample text.
```

## Helpful links
- [Pytesseract Documentation](https://pypi.org/project/pytesseract/)
- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract)

onelinerhub: [How can I use Tesseract OCR with Python?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-with-python)