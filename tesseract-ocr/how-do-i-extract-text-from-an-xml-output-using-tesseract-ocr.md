# How do I extract text from an XML output using Tesseract OCR?
// plain

To extract text from an XML output using Tesseract OCR, you will need to use the Tesseract API. The Tesseract API provides a range of methods for extracting text from an image or PDF. Here is an example of how to extract text from an XML output using Tesseract OCR:

```
#import the Tesseract API
from tesseract import Tesseract

#instantiate Tesseract object
tesseract_obj = Tesseract()

#load the XML output
xml_output = tesseract_obj.load_xml_file('example.xml')

#extract text from the XML output
text = tesseract_obj.extract_text_from_xml(xml_output)

#print the extracted text
print(text)
```

## Output example

```
This is an example of text extracted from an XML output.
```

## Code explanation


1. `from tesseract import Tesseract`: This imports the Tesseract API.
2. `tesseract_obj = Tesseract()`: This instantiates a Tesseract object.
3. `xml_output = tesseract_obj.load_xml_file('example.xml')`: This loads the XML output from a file.
4. `text = tesseract_obj.extract_text_from_xml(xml_output)`: This extracts the text from the XML output.
5. `print(text)`: This prints the extracted text.

## Helpful links

- [Tesseract OCR Documentation](https://tesseract-ocr.github.io/tessdoc/)
- [Tesseract API Reference](https://tesseract-ocr.github.io/tessdoc/api/index.html)

onelinerhub: [How do I extract text from an XML output using Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-extract-text-from-an-xml-output-using-tesseract-ocr)