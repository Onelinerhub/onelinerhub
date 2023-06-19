# How do I use tesseract OCR in an iOS app?
// plain

Tesseract OCR (Optical Character Recognition) can be used in an iOS app by following these steps:

1. Download the **Tesseract OCR iOS framework** from the [GitHub repository](https://github.com/gali8/Tesseract-OCR-iOS).

2. Add the framework to your project by dragging the `TesseractOCR.framework` folder into your project in XCode.

3. Create an instance of `G8Tesseract` and set the language, for example:
```
let tesseract = G8Tesseract(language: "eng")
```

4. Set the image to be recognized:
```
tesseract.image = UIImage(named: "sampleImage")
```

5. Recognize the text:
```
tesseract.recognize()
```

6. Get the recognized text:
```
let recognizedText = tesseract.recognizedText
```

7. Finally, print the recognized text:
```
print(recognizedText)
```

The output would be the recognized text from the image.

onelinerhub: [How do I use tesseract OCR in an iOS app?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-in-an-ios-app)