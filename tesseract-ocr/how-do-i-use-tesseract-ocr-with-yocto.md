# How do I use tesseract-ocr with yocto?
// plain

Tesseract-OCR is a powerful open source Optical Character Recognition (OCR) engine that can be used with Yocto.

In order to use Tesseract-OCR with Yocto, you must first install the `tesseract-ocr` package. This can be done by adding `tesseract-ocr` to the `IMAGE_INSTALL_append` variable in your Yocto project's `local.conf` file.

For example:
```
IMAGE_INSTALL_append = " tesseract-ocr"
```

Once the package is installed, you can use the `tesseract` command to process images. For example, to recognize text in an image file called `image.png`:

```
tesseract image.png output
```

The above command will create a text file called `output.txt` with the recognized text.

The following parts are involved in using Tesseract-OCR with Yocto:
- Installing the `tesseract-ocr` package by adding it to the `IMAGE_INSTALL_append` variable in the `local.conf` file.
- Using the `tesseract` command to process images.

## Helpful links
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
- [Yocto Project](https://www.yoctoproject.org/)

onelinerhub: [How do I use tesseract-ocr with yocto?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-with-yocto)