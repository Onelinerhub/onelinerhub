# How do I configure the output format of tesseract OCR?
// plain

```
# include tesseract library
import tesseract

# set output format to hocr
api = tesseract.TessBaseAPI()
api.SetPageSegMode(tesseract.PSM_AUTO)
api.SetOutputFormat(tesseract.RIL_HOCR)

# run tesseract with image file
api.SetImageFile('my_image.png')
api.Recognize()

# get output
text = api.GetUTF8Text()

# print output
print(text)
```

The above example code will configure the output format of tesseract OCR to hOCR (HTML-based Open Document Format for the Recognition of Text). It will also run tesseract with an image file `my_image.png` and print the output.

The code consists of the following parts:
1. `import tesseract`: This imports the tesseract library.
2. `api = tesseract.TessBaseAPI()`: This creates an instance of the TessBaseAPI class.
3. `api.SetPageSegMode(tesseract.PSM_AUTO)`: This sets the page segmentation mode to auto.
4. `api.SetOutputFormat(tesseract.RIL_HOCR)`: This sets the output format to hOCR.
5. `api.SetImageFile('my_image.png')`: This sets the image file to the given file.
6. `api.Recognize()`: This runs tesseract on the given image file.
7. `text = api.GetUTF8Text()`: This gets the output in UTF-8 encoded text.
8. `print(text)`: This prints the output.

For more information on configuring the output format of tesseract OCR, please refer to the following links:

- [Tesseract OCR Documentation](https://tesseract-ocr.github.io/tessdoc/Home.html)
- [Tesseract OCR Output Formats](https://tesseract-ocr.github.io/tessdoc/OutputFormats.html)

onelinerhub: [How do I configure the output format of tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-configure-the-output-format-of-tesseract-ocr)