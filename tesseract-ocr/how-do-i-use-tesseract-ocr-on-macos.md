# How do I use Tesseract OCR on macOS?
// plain

Tesseract OCR is an open source OCR library that can be used on macOS. It can be installed using Homebrew:

```
brew install tesseract
```

Once installed, you can use Tesseract to recognize text from an image file. For example, the following command will recognize text from an image file called `example.png`:

```
tesseract example.png output
```

This command will output a file called `output.txt` that contains the recognized text.

You can also specify the language of the text to be recognized. For example, to recognize German text, you can use the following command:

```
tesseract example.png output -l deu
```

You can find a list of available languages [here](https://github.com/tesseract-ocr/tessdata/tree/3.04.00).

You can also adjust the OCR engine mode to optimize for different types of text. For example, to optimize for a single uniform block of text, you can use the following command:

```
tesseract example.png output -psm 6
```

You can find a list of available OCR engine modes [here](https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage#basic-usage).

Tesseract OCR can also be used with other programming languages such as Python and Java. For more information, you can refer to the [official documentation](https://github.com/tesseract-ocr/tesseract/wiki).

onelinerhub: [How do I use Tesseract OCR on macOS?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-on-macos)