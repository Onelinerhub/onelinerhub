# How do I use Tesseract OCR with Yum?
// plain

Using Tesseract OCR with Yum is a relatively simple process. Here is an example of how to do it:

```
# Install Tesseract OCR
sudo yum install -y tesseract

# Check the version of Tesseract OCR
tesseract -v
```

The output of this command should look something like this:
```
tesseract 4.1.1
 leptonica-1.78.0
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.2) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11 : libwebp 0.6.1 : libopenjp2 2.3.0
 Found AVX2
 Found AVX
 Found SSE
```

This indicates that Tesseract OCR version 4.1.1 has been installed.

## Code explanation


- `sudo yum install -y tesseract`: This command installs Tesseract OCR using Yum.
- `tesseract -v`: This command checks the version of Tesseract OCR installed.

Here are some useful links for further information:

- [Tesseract OCR Installation Guide](https://tesseract-ocr.github.io/tessdoc/Home.html)
- [Yum Command Manual](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sec-managing_software_with_yum)

onelinerhub: [How do I use Tesseract OCR with Yum?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-with-yum)