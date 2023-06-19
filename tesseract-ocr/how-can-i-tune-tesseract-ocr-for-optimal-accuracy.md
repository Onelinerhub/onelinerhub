# How can I tune Tesseract OCR for optimal accuracy?
// plain

Tesseract OCR can be tuned for optimal accuracy by adjusting the parameters of the Tesseract engine. Here are some of the most important parameters to consider:

1. **Page Segmentation Mode:** This parameter determines how Tesseract will interpret the page layout. The default is `PSM_AUTO` which works well in most cases, but for improved accuracy you can set it to `PSM_SINGLE_BLOCK` or `PSM_SINGLE_LINE` depending on the type of document you are trying to process.

2. **Language:** Specifying the language of the document can help Tesseract recognize the text more accurately. For example, you can set the language parameter to `eng` if the document is in English.

3. **OEM:** This parameter determines the type of OCR engine that Tesseract will use. The default is `OEM_DEFAULT`, but for improved accuracy you can set it to `OEM_TESSERACT_ONLY` or `OEM_LSTM_ONLY`.

4. **Whitelist:** If you know the characters that are present in the document, you can specify them in the whitelist parameter to help Tesseract recognize them more accurately.

Here is an example of how to set these parameters in Python:

```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(
    image,
    lang='eng',
    config='--psm 11 --oem 3 --whitelist ABCDEFGHIJKLMNOPQRSTUVWXYZ',
)
```

## Helpful links

- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract/wiki)
- [pytesseract Documentation](https://pypi.org/project/pytesseract/)

onelinerhub: [How can I tune Tesseract OCR for optimal accuracy?](https://onelinerhub.com/tesseract-ocr/how-can-i-tune-tesseract-ocr-for-optimal-accuracy)