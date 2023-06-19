# How can I use Tesseract OCR with Node.js?
// plain

Using Tesseract OCR with Node.js is possible thanks to the Tesseract.js library. Tesseract.js is a JavaScript library that wraps the Tesseract OCR engine. It allows you to use the Tesseract OCR engine in Node.js applications. Here's an example of how to use Tesseract.js in Node.js:

```
const { TesseractWorker } = require("tesseract.js");
const worker = new TesseractWorker();

worker
  .recognize("example.png")
  .progress(message => {
    console.log(message);
  })
  .then(result => {
    console.log(result.text);
  })
  .finally(() => worker.terminate());
```

This code will recognize the text in the example.png image and output it in the console.

The code consists of the following parts:

1. `const { TesseractWorker } = require("tesseract.js");` - this line imports the TesseractWorker class from the tesseract.js library.

2. `const worker = new TesseractWorker();` - this line creates a new instance of the TesseractWorker class.

3. `worker.recognize("example.png")` - this line calls the recognize() method of the worker instance, passing in the path to the image that should be recognized.

4. `.progress(message => { console.log(message); })` - this line adds a progress handler to the worker instance. This handler will be called each time the OCR engine makes progress and will output the progress message to the console.

5. `.then(result => { console.log(result.text); })` - this line adds a then handler to the worker instance. This handler will be called when the OCR engine is done and will output the recognized text to the console.

6. `.finally(() => worker.terminate());` - this line adds a finally handler to the worker instance. This handler will be called when the OCR engine is done and will terminate the worker instance.

For more information about Tesseract.js and how to use it in Node.js applications, please refer to the following links:

- [Tesseract.js Documentation](https://tesseract.projectnaptha.com/docs.html)
- [Node.js Tutorial](https://www.tutorialspoint.com/nodejs/index.htm)

onelinerhub: [How can I use Tesseract OCR with Node.js?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-with-node-js)