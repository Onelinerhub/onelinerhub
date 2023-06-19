# How do I use Tesseract OCR with JavaScript?
// plain

Tesseract OCR (Optical Character Recognition) is a powerful open source software library for reading text from images. It can be used with JavaScript for extracting text from images.

To use Tesseract OCR with JavaScript, you need to install the Tesseract.js library. It is a JavaScript port of the popular Tesseract OCR engine.

## Example code

```
const Tesseract = require('tesseract.js');
const image = 'path/to/image.png';

Tesseract.recognize(image)
  .progress(function  (p) { console.log('progress', p)  })
  .then(function (result) {
    console.log(result.text);
  })
```

The code above loads the Tesseract.js library, defines the path to the image and then calls the recognize() function. The progress() function is used to display the progress of the recognition process, and the then() function is used to display the extracted text.

## Code explanation

- `const Tesseract = require('tesseract.js');`: Loads the Tesseract.js library.
- `const image = 'path/to/image.png';`: Defines the path to the image.
- `Tesseract.recognize(image)`: Calls the recognize() function.
- `.progress(function  (p) { console.log('progress', p)  })`: Displays the progress of the recognition process.
- `.then(function (result) { console.log(result.text); })`: Displays the extracted text.

## Helpful links
- [Tesseract.js](https://github.com/naptha/tesseract.js)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

onelinerhub: [How do I use Tesseract OCR with JavaScript?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-with-javascript)