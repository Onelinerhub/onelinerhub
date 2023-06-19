# How do I use Tesseract OCR for Android?
// plain

Tesseract OCR (Optical Character Recognition) is an open source library for Android that can be used to detect and recognize text from images. It can be used to create an application that can read text from images or documents.

To use Tesseract OCR for Android, you need to add the Tesseract library to your project. You can do this by adding the following line to your project's build.gradle file:

```
implementation 'com.rmtheis:tess-two:9.0.0'
```

Once the library is added, you can create a TessBaseAPI object and use it to detect and recognize text from an image. The following example code shows how to do this:

```
TessBaseAPI tessBaseAPI = new TessBaseAPI();
tessBaseAPI.init(dataPath, language);
tessBaseAPI.setImage(bitmap);
String recognizedText = tessBaseAPI.getUTF8Text();
```

The code above will create a TessBaseAPI object and initialize it with the path to the Tesseract data files and the language to be used for recognition. It will then set the image to be processed and finally get the recognized text as a UTF-8 string.

## Helpful links
- Tesseract OCR for Android: https://github.com/rmtheis/tess-two
- Tesseract Wiki: https://github.com/tesseract-ocr/tesseract/wiki

onelinerhub: [How do I use Tesseract OCR for Android?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-for-android)