# How can I configure Tesseract OCR options?
// plain

Tesseract OCR options can be configured using the command line interface. The basic command structure is `tesseract imagename outputbase [-l lang] [options]` where `imagename` is the image file to be processed, `outputbase` is the output file name, `lang` is the language of the text in the image, and `options` are any additional options.

For example, to configure Tesseract to output the text in a PDF file, the command would be:

```
tesseract imagename outputbase.pdf -l eng pdf
```

The `-l` option sets the language of the text in the image, and the `pdf` option specifies that the output should be a PDF file.

Additional options can be passed to Tesseract to customize the OCR output. For example, to set the page segmentation mode to single line, the option `--psm 6` can be used.

```
tesseract imagename outputbase.pdf -l eng pdf --psm 6
```

The full list of options can be found in the [Tesseract documentation](https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage).

The options can also be set in a configuration file using the `-c` option. For example, to set the page segmentation mode to single line, the configuration file would look like this:

```
tessedit_pageseg_mode 6
```

The configuration file can then be passed to Tesseract using the `-c` option:

```
tesseract imagename outputbase.pdf -l eng pdf -c config.txt
```

These options can be used to customize the output of Tesseract OCR.

onelinerhub: [How can I configure Tesseract OCR options?](https://onelinerhub.com/tesseract-ocr/how-can-i-configure-tesseract-ocr-options)