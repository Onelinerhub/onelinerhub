# How do I create a demo of Tesseract OCR?
// plain

1. Download and install Tesseract OCR from [this link](https://github.com/tesseract-ocr/tesseract/wiki).
2. Create a Python file, `demo.py` and insert the following code block:
```python
import pytesseract
from PIL import Image

# Load image
image = Image.open("sample.png")

# Run Tesseract OCR
text = pytesseract.image_to_string(image)

# Print the recognized text
print(text)
```
3. Run the script with `python demo.py` to get the recognized text from the input image `sample.png`:
```
This is a sample text
```
4. To improve the accuracy of the output, you can pass additional parameters to the `image_to_string` function, such as `lang` (for the language of the text) and `config` (for custom configurations).
5. To learn more about Tesseract OCR and its usage, refer to [this guide](https://realpython.com/python-pytesseract/).
6. To test the accuracy of your OCR model, you can use the [Tesseract Evaluation Tool](https://github.com/tesseract-ocr/tesseract/wiki/Evaluation-Tools).
7. For further information, you can also refer to [this tutorial](https://www.learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/).

onelinerhub: [How do I create a demo of Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-create-a-demo-of-tesseract-ocr)