# How can I use UiPath to implement Tesseract OCR language processing?
// plain

UiPath can be used to implement Tesseract OCR language processing by using the Tesseract activities. These activities provide the ability to recognize text from images, PDFs, and other documents. The Tesseract activities can be used to:

1. Extract text from images and documents.
2. Train the Tesseract engine to recognize different languages.
3. Use the trained engine to recognize text in different languages.

## Example code


```
TesseractEngine engine = new TesseractEngine("C:\\tessdata", "eng", EngineMode.Default);

Page page = engine.Process(@"C:\myImage.png");

Console.WriteLine(page.GetText());
```

## Output example

```
This is an example of text extracted from an image.
```

The code above creates a new Tesseract engine, processes an image and prints out the recognized text.

## Helpful links

- [UiPath Tesseract activities](https://activities.uipath.com/docs/tesseract-activities)
- [Tesseract OCR Language Processing](https://www.tesseract-ocr.com/docs/langproc.html)

onelinerhub: [How can I use UiPath to implement Tesseract OCR language processing?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-uipath-to-implement-tesseract-ocr-language-processing)