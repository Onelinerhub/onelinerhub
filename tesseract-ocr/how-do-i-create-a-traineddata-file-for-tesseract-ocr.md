# How do I create a traineddata file for Tesseract OCR?
// plain

Creating a traineddata file for Tesseract OCR requires a few steps:

1. Generate a font_properties file. This file contains information about the font family, font style, font weight, font size, and font language.

```
familyname fontname bold italic size language

## Example


Roboto Regular normal normal 48 eng
```

2. Generate a box file. This file contains information about the characters in the font. It is generated from the font_properties file.

```
tesseract fontname.font_properties fontname.box

## Example


tesseract Roboto.font_properties Roboto.box
```

3. Generate the traineddata file. This file is generated from the box file.

```
combine_tessdata -e fontname.traineddata fontname.

## Example


combine_tessdata -e Roboto.traineddata Roboto.
```

4. Test the traineddata file. This step is optional, but it is recommended to ensure that the traineddata file is working properly.

```
tesseract --tessdata-dir . fontname.exp0.tif fontname.exp0 -l fontname

## Example


tesseract --tessdata-dir . Roboto.exp0.tif Roboto.exp0 -l Roboto
```

The output should be a text file containing the text from the image.

## Helpful links

- [Tesseract Tutorial](https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract-4.00#how-to-create-a-traineddata-file)
- [Tesseract Documentation](https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc)

onelinerhub: [How do I create a traineddata file for Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-create-a-traineddata-file-for-tesseract-ocr)