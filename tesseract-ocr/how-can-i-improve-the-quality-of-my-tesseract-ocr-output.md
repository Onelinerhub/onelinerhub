# How can I improve the quality of my Tesseract OCR output?
// plain

1. **Increase the resolution of the input image.** Higher resolution images will result in better Tesseract OCR output, as the text will be more clear and readable.

2. **Adjust the image contrast.** Increasing the contrast of the image can help Tesseract OCR to better distinguish between the text and the background.

3. **Use a pre-processing filter.** Using a pre-processing filter such as a Gaussian blur can help Tesseract OCR to better recognize the text.

4. **Apply image binarization.** Applying image binarization can help Tesseract OCR to better identify the text in the image.

5. **Include language-specific training data.** Including language-specific training data can help Tesseract OCR to better recognize the text in the image.

6. **Use a language-specific configuration file.** Using a language-specific configuration file can help Tesseract OCR to better recognize the text in the image.

7. **Adjust the Tesseract OCR parameters.** Adjusting the Tesseract OCR parameters such as the page segmentation mode, the oem mode, and the tesseract config file can help to improve the quality of the Tesseract OCR output.

## Example code

```
tesseract image.jpg output --psm 6 --oem 1 --tessconfig config.conf
```
## Output example

```
Tesseract Open Source OCR Engine v5.0.0-alpha.20200328 with Leptonica
```

onelinerhub: [How can I improve the quality of my Tesseract OCR output?](https://onelinerhub.com/tesseract-ocr/how-can-i-improve-the-quality-of-my-tesseract-ocr-output)