# How can I use Tesseract OCR on a Raspberry Pi?
// plain

Using Tesseract OCR on a Raspberry Pi is quite simple.

1. Install Tesseract OCR:

```
sudo apt-get install tesseract-ocr
```

## Output example


```
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libleptonica-dev libtesseract-dev tesseract-ocr-eng
Suggested packages:
  tesseract-ocr-osd tesseract-ocr-spa tesseract-ocr-chi-sim
  tesseract-ocr-chi-tra tesseract-ocr-equ
The following NEW packages will be installed:
  libleptonica-dev libtesseract-dev tesseract-ocr tesseract-ocr-eng
0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/1,926 kB of archives.
After this operation, 9,848 kB of additional disk space will be used.
Do you want to continue? [Y/n]
```

2. Set up the language:

```
sudo apt-get install tesseract-ocr-eng
```

## Output example


```
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libleptonica-dev libtesseract-dev tesseract-ocr
Suggested packages:
  tesseract-ocr-osd tesseract-ocr-spa tesseract-ocr-chi-sim
  tesseract-ocr-chi-tra tesseract-ocr-equ
The following NEW packages will be installed:
  libleptonica-dev libtesseract-dev tesseract-ocr tesseract-ocr-eng
0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/1,926 kB of archives.
After this operation, 9,848 kB of additional disk space will be used.
Do you want to continue? [Y/n]
```

3. Run Tesseract OCR:

```
tesseract image.jpg output
```

This will output a text file named 'output.txt' that contains the text extracted from the image.

## Helpful links

- [Tesseract OCR on Raspberry Pi](https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/)
- [Tesseract OCR Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki/Compiling)

onelinerhub: [How can I use Tesseract OCR on a Raspberry Pi?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-on-a-raspberry-pi)