# How can I use Tesseract OCR to set the Page Segmentation Mode (PSM) for an image?
// plain

To use Tesseract OCR to set the Page Segmentation Mode (PSM) for an image, you will need to use the `tesseract_cmd.SetPageSegMode()` method. This method takes a single argument, which is an integer representing the desired page segmentation mode.

For example, to set the PSM to single line mode, you would use the following code:

```
import tesseract_cmd

api = tesseract_cmd.TessBaseAPI()
api.SetPageSegMode(tesseract_cmd.PSM_SINGLE_LINE)
```

The `PSM_SINGLE_LINE` constant is defined in the `tesseract_cmd` module and is used to indicate the single line page segmentation mode. Other constants that can be used to set the page segmentation mode are:

* `PSM_AUTO`: Automatically detect the page segmentation mode
* `PSM_SINGLE_BLOCK`: Treat the image as a single text line
* `PSM_SINGLE_CHAR`: Treat the image as a single word
* `PSM_SINGLE_COLUMN`: Treat the image as a single column of text
* `PSM_SINGLE_BLOCK_VERT_TEXT`: Treat the image as a single block of vertically aligned text
* `PSM_SPARSE_TEXT`: Treat the image as a sparse text
* `PSM_SPARSE_TEXT_OSD`: Treat the image as a sparse text with orientation and script detection

For more information about the different page segmentation modes and how to use them, please refer to the [Tesseract OCR documentation](https://github.com/tesseract-ocr/tesseract/wiki/PageSegMode).

onelinerhub: [How can I use Tesseract OCR to set the Page Segmentation Mode (PSM) for an image?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-to-set-the-page-segmentation-mode--psm--for-an-image)