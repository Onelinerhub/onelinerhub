# How can I use Homebrew to install Tesseract OCR?
// plain

Homebrew is a package manager for macOS. It can be used to install Tesseract OCR with the following steps:

1. Open the Terminal application.
2. Type `brew update` and press enter. This will update Homebrew with the latest packages.
3. Type `brew install tesseract` and press enter. This will install Tesseract OCR.
4. To test the installation, type `tesseract --version` and press enter. This should output the version of Tesseract OCR installed.

## Example code

```
brew update
brew install tesseract
tesseract --version
```

Example output:
```
tesseract 4.1.1
 leptonica-1.78.0
  libgif 5.2.1 : libjpeg 8d (libjpeg-turbo 1.5.2) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11
```

- `brew update`: Updates Homebrew with the latest packages.
- `brew install tesseract`: Installs Tesseract OCR.
- `tesseract --version`: Outputs the version of Tesseract OCR installed.

## Helpful links
- Homebrew: https://brew.sh/
- Tesseract OCR: https://github.com/tesseract-ocr/tesseract

onelinerhub: [How can I use Homebrew to install Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-homebrew-to-install-tesseract-ocr)