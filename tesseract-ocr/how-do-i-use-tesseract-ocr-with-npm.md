# How do I use Tesseract OCR with NPM?
// plain

Tesseract OCR is an open source Optical Character Recognition (OCR) engine that can be used to recognize text in images. It can be used with Node.js and NPM (Node Package Manager) to extract text from images.

To use Tesseract OCR with NPM, you need to install the tesseract.js package. This can be done by running the following command in the terminal:

```
$ npm install tesseract.js
```

Once the package is installed, you can use the Tesseract.recognize() method to extract text from an image. For example, the following code will extract text from a sample image:

```
const { TesseractWorker } = require('tesseract.js');
const worker = new TesseractWorker();

(async () => {
  const { text } = await worker.recognize('sample.png');
  console.log(text);
})();
```

The output of the above code will be the text extracted from the sample image.

The code consists of the following parts:

1. `const { TesseractWorker } = require('tesseract.js');`: This imports the TesseractWorker class from the tesseract.js package.

2. `const worker = new TesseractWorker();`: This creates an instance of the TesseractWorker class.

3. `await worker.recognize('sample.png');`: This calls the TesseractWorker's recognize() method to extract text from the sample image.

4. `console.log(text);`: This prints the extracted text to the console.

For more information about using Tesseract OCR with NPM, please refer to the following links:

- [Tesseract.js Documentation](https://tesseract.projectnaptha.com/docs.html)
- [Tesseract.js Github Repo](https://github.com/naptha/tesseract.js)

onelinerhub: [How do I use Tesseract OCR with NPM?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-with-npm)