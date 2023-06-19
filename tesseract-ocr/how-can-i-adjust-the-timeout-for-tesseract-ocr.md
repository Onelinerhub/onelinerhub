# How can I adjust the timeout for Tesseract OCR?
// plain

Tesseract OCR can be configured to set a timeout for each recognition process.

To adjust the timeout, set the `tessedit_timeout_milliseconds` parameter in the Tesseract configuration file. The default value is 0, which indicates no timeout.

For example, to set the timeout to 10 seconds, the configuration file should contain the following line:

```
tessedit_timeout_milliseconds 10000
```

## Code explanation


- `tessedit_timeout_milliseconds`: The parameter used to set the timeout for Tesseract OCR.
- `10000`: The value for the timeout in milliseconds (10 seconds).

For more information about Tesseract configuration parameters, please refer to the [Tesseract documentation](https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality#configuration-parameters).

onelinerhub: [How can I adjust the timeout for Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-can-i-adjust-the-timeout-for-tesseract-ocr)