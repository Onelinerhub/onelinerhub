# How do I use Tesseract OCR to recognize text in an image?
// plain

Tesseract OCR (Optical Character Recognition) is a powerful open source library for recognizing text in an image. It can be used with Python, Java, and C++. Here is an example of how to use Tesseract OCR with Python:

```
# import the pytesseract module
import pytesseract

# Provide path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Read image from which text needs to be extracted
image = cv2.imread('image.png')

# Run tesseract OCR on image
text = pytesseract.image_to_string(image)

# Print recognized text
print(text)
```

## Output example

```
This is a sample text.
```

The code above reads an image and uses Tesseract OCR to extract the text from it. Here are the parts of the code and what they do:

1. `import pytesseract`: imports the pytesseract module which contains functions for using Tesseract OCR.
2. `pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`: provides the path to the Tesseract executable.
3. `image = cv2.imread('image.png')`: reads the image from which text needs to be extracted.
4. `text = pytesseract.image_to_string(image)`: runs Tesseract OCR on the image and extracts the text.
5. `print(text)`: prints the recognized text.

For more information on using Tesseract OCR, please refer to the [official documentation](https://tesseract-ocr.github.io/tessdoc/Home.html).

onelinerhub: [How do I use Tesseract OCR to recognize text in an image?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-to-recognize-text-in-an-image)