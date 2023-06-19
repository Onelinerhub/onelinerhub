# How to use Tesseract OCR with Flutter?
// plain

Tesseract OCR is an open source optical character recognition (OCR) engine that can be used with Flutter. It can be used to detect text from images, convert scanned documents into editable text, and extract text from PDFs.

To use Tesseract OCR with Flutter, you will need to install the tesseract-ocr-flutter plugin. This plugin is available on pub.dev, so you can install it by adding the following line to your pubspec.yaml file:

```
dependencies:
  tesseract_ocr_flutter: ^1.0.1
```

Once the plugin is installed, you can use the Tesseract OCR API to detect text from an image. For example, the following code will detect the text from an image file stored in the assets folder:

```
String text;

TesseractOcr.detect("assets/image.png").then((value) {
  text = value;
});
```

The output of this code will be a String containing the detected text.

In addition to detecting text from images, the Tesseract OCR plugin also provides APIs for recognizing text from PDFs, recognizing text from a camera stream, and recognizing text from a live camera stream.

## Helpful links
- https://pub.dev/packages/tesseract_ocr_flutter
- https://github.com/tesseract-ocr/tesseract/wiki/APIExample

onelinerhub: [How to use Tesseract OCR with Flutter?](https://onelinerhub.com/tesseract-ocr/how-to-use-tesseract-ocr-with-flutter)