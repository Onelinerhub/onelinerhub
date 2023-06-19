# How do I install Tesseract OCR on my Mac?
// plain

To install Tesseract OCR on your Mac, follow these steps:
1. Install Homebrew:
   ```
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ```
   Output: Homebrew is installed!

2. Install Tesseract OCR using Homebrew:
   ```
   brew install tesseract
   ```
   Output: Updating Homebrew...
           ==> Downloading https://homebrew.bintray.com/bottles/tesseract-4.1.1.catalina.bottle.tar.gz
           ==> Pouring tesseract-4.1.1.catalina.bottle.tar.gz
           ==> Caveats
           Please add the following to your .bash_profile:
           export TESSDATA_PREFIX=/usr/local/opt/tesseract/share/tessdata

3. Set Tesseract environment variable:
   ```
   export TESSDATA_PREFIX=/usr/local/opt/tesseract/share/tessdata
   ```

4. Verify installation:
   ```
   tesseract -v
   ```
   Output: tesseract 4.1.1

## Helpful links
- [Homebrew installation instructions](https://brew.sh/index_ja)
- [Tesseract Documentation](https://tesseract-ocr.github.io/tessdoc/)

onelinerhub: [How do I install Tesseract OCR on my Mac?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-tesseract-ocr-on-my-mac)