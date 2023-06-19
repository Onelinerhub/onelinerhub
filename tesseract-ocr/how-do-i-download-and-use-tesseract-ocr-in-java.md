# How do I download and use Tesseract OCR in Java?
// plain

1. Download the Tesseract OCR library from the [Tesseract GitHub page](https://github.com/tesseract-ocr/tesseract).
2. Add the Tesseract library to your Java project.
3. Create an instance of the Tesseract library and set the language to use:
```
ITesseract instance = new Tesseract();
instance.setLanguage("eng");
```
4. Load the image to process:
```
File imageFile = new File("image.png");
```
5. Run the Tesseract library on the image:
```
String result = instance.doOCR(imageFile);
```
6. Print the result:
```
System.out.println(result);
```
7. The output will be the text contained in the image.

onelinerhub: [How do I download and use Tesseract OCR in Java?](https://onelinerhub.com/tesseract-ocr/how-do-i-download-and-use-tesseract-ocr-in-java)