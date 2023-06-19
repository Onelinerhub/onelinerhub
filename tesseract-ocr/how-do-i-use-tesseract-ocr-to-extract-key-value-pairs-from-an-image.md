# How do I use Tesseract OCR to extract key-value pairs from an image?
// plain

Using Tesseract OCR to extract key-value pairs from an image is a relatively simple process. The following example code shows how to use the Tesseract OCR library to extract text from an image and then use a regular expression to extract key-value pairs.

```
import pytesseract
import re

# Read image
img = cv2.imread('image.png')

# Extract text from image
text = pytesseract.image_to_string(img)

# Extract key-value pairs from text
pairs = re.findall(r'(\w+)\s*:\s*(\w+)', text)

# Print pairs
print(pairs)
```

## Output example


```
[('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]
```

The code above does the following:

1. Imports the `pytesseract` and `re` libraries.
2. Reads the image from the file `image.png`.
3. Uses `pytesseract.image_to_string()` to extract the text from the image.
4. Uses a regular expression to extract key-value pairs from the text.
5. Prints out the extracted pairs.

## Helpful links

- [pytesseract documentation](https://github.com/madmaze/pytesseract)
- [Regular Expression Documentation](https://docs.python.org/3/library/re.html)

onelinerhub: [How do I use Tesseract OCR to extract key-value pairs from an image?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-to-extract-key-value-pairs-from-an-image)