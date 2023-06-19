# How do I use the online demo of Tesseract OCR?
// plain

**Using the online demo of Tesseract OCR**

1. Go to the [Tesseract OCR online demo](https://tesseract-ocr.github.io/tesseract.js-demo/) page.
2. Upload an image by clicking the “Choose File” button.
3. Select the language of the text in the image from the drop-down menu.
4. Click the “Recognize” button to start the OCR process.
5. The recognized text will be displayed in the text box below the image.

## Example code

```
const tesseract = require('tesseract.js')
const image = 'path/to/image.jpg'

tesseract.recognize(image, {
  lang: 'eng'
}).then(({ data: { text } }) => {
  console.log(text)
})
```

## Output example

```
This is a sample text.
```

The code above uses the `tesseract.js` library to recognize text from an image. It takes the path to the image and the language of the text as parameters. It then returns the recognized text in the `text` variable.

## Helpful links
- [Tesseract OCR online demo](https://tesseract-ocr.github.io/tesseract.js-demo/)
- [tesseract.js Documentation](https://tesseract.projectnaptha.com/)

onelinerhub: [How do I use the online demo of Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-the-online-demo-of-tesseract-ocr)