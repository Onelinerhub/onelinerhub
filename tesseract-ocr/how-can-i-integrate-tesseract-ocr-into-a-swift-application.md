# How can I integrate Tesseract OCR into a Swift application?
// plain

Integrating Tesseract OCR into a Swift application is relatively straightforward. The following steps outline the process:

1. Install the [Tesseract OCR iOS](https://github.com/gali8/Tesseract-OCR-iOS) library.
2. Import the `TesseractOCR.h` and `TesseractOCR.m` files into the project.
3. Initialize the TesseractOCR class and set the language.
```swift
let tesseract = G8Tesseract(language: "eng")
```
4. Pass the image to the TesseractOCR class and recognize it.
```swift
tesseract.image = image
tesseract.recognize()
```
5. Get the recognized text from the TesseractOCR class.
```swift
let recognizedText = tesseract.recognizedText
```
6. Display the recognized text.
```swift
print(recognizedText)
```
7. Cleanup the TesseractOCR class after use.
```swift
tesseract.clear()
```

## Helpful links
- [Tesseract OCR iOS](https://github.com/gali8/Tesseract-OCR-iOS)
- [Integrating Tesseract OCR into iOS App](https://www.raywenderlich.com/1464-tesseract-ocr-tutorial-for-ios)

onelinerhub: [How can I integrate Tesseract OCR into a Swift application?](https://onelinerhub.com/tesseract-ocr/how-can-i-integrate-tesseract-ocr-into-a-swift-application)