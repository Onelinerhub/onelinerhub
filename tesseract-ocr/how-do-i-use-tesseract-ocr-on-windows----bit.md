# How do I use tesseract OCR on Windows 64-bit?
// plain

To use tesseract OCR on Windows 64-bit, you need to install the tesseract OCR engine and the tesseract language data files.

1. Download and install the tesseract OCR engine from [this link](https://github.com/UB-Mannheim/tesseract/wiki).
2. Download and install the language data files from [this link](https://github.com/tesseract-ocr/tessdata).
3. Set the `TESSDATA_PREFIX` environment variable to the directory where the language data files are installed.

Once the installation is complete, you can use the tesseract command line tool to extract text from an image. For example, to extract text from an image called `image.png`, you can use the following command:

```
tesseract image.png output
```

This will create a text file called `output.txt` in the same directory with the extracted text.

You can also use the tesseract API to integrate tesseract OCR into your own applications. For example, the following code snippet shows how to use the tesseract API to extract text from an image file:

```python
import tesseract

api = tesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)

mImgFile = "image.png"
image = tesseract.pixRead(mImgFile)
api.SetImage(image)
text = api.GetUTF8Text()
print(text)
```

The output of the above code would be the text extracted from the image file.

onelinerhub: [How do I use tesseract OCR on Windows 64-bit?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-on-windows----bit)