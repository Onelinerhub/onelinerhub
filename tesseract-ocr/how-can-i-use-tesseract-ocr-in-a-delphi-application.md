# How can I use Tesseract OCR in a Delphi application?
// plain

You can use Tesseract OCR in a Delphi application by using the [Tesseract OCR API for Delphi](https://github.com/B-Con/tesseract-ocr-for-delphi). This API provides a Delphi component that wraps the Tesseract OCR library.

To use the API, you need to install the Tesseract OCR library and the API. Once these are installed, you can use the API in your Delphi application.

Here is an example of how to use the API to recognize text from an image:

```
uses
  TesseractOCR;

var
  TesseractOCR: TTesseractOCR;
  Text: string;
begin
  TesseractOCR := TTesseractOCR.Create;
  try
    TesseractOCR.ImagePath := 'image.png';
    TesseractOCR.Recognize;
    Text := TesseractOCR.Text;
  finally
    TesseractOCR.Free;
  end;
end;
```

This code will create an instance of the `TTesseractOCR` class, set the `ImagePath` property to the path of the image to be recognized, call the `Recognize` method to perform the actual recognition, and then store the recognized text in the `Text` property.

## Helpful links

- [Tesseract OCR API for Delphi](https://github.com/B-Con/tesseract-ocr-for-delphi)
- [Tesseract OCR Library](https://github.com/tesseract-ocr/tesseract)

onelinerhub: [How can I use Tesseract OCR in a Delphi application?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-in-a-delphi-application)