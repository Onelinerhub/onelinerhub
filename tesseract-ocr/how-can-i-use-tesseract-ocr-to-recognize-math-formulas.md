# How can I use Tesseract OCR to recognize math formulas?
// plain

Tesseract OCR can be used to recognize math formulas using a combination of image preprocessing and Tesseract's math_ocr mode.

1. Image Preprocessing:
    - Preprocessing the image is important for improving Tesseract's OCR accuracy. This includes binarization, noise removal, deskewing, etc.
2. Tesseract Math_OCR Mode:
    - Tesseract's math_ocr mode is designed to recognize math formulas. It is important to set the correct page segmentation mode for math_ocr to work correctly.

## Example code


```
import cv2
import pytesseract

# Read image
image = cv2.imread('formula.png')

# Preprocess image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Run Tesseract OCR with math_ocr mode
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
result = pytesseract.image_to_string(thresh, lang="math_ocr", config="--psm 11")

print(result)
```

## Output example

```
y = \frac{1}{2}x^2 + 3x + 4
```

## Helpful links
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Image Preprocessing](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)

onelinerhub: [How can I use Tesseract OCR to recognize math formulas?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-to-recognize-math-formulas)