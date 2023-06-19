# How can I use UiPath and Tesseract OCR together to automate a process?
// plain

UiPath and Tesseract OCR can be used together to automate a process by leveraging the power of both. UiPath is a robotic process automation (RPA) tool that can be used to automate processes by acting as a virtual machine that can interact with the user interface. Tesseract OCR is an open-source optical character recognition (OCR) tool that can be used to extract text from images.

To use UiPath and Tesseract OCR together to automate a process, the following steps can be followed:

1. Use UiPath to take a screenshot of the text to be extracted.
2. Use UiPath to save the screenshot to a file.
3. Use Tesseract OCR to extract the text from the screenshot file.

## Example code

```
# Step 1: Take a screenshot of the text to be extracted
screenshot = UiPath.TakeScreenshot()

# Step 2: Save the screenshot to a file
UiPath.SaveScreenshot(screenshot, "screenshot.png")

# Step 3: Extract the text from the screenshot file
text = Tesseract.ExtractText("screenshot.png")

# Output
print(text)
```
## Output example

```
This is the text to be extracted.
```

## Helpful links

- UiPath: https://www.uipath.com/
- Tesseract OCR: https://github.com/tesseract-ocr/tesseract

onelinerhub: [How can I use UiPath and Tesseract OCR together to automate a process?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-uipath-and-tesseract-ocr-together-to-automate-a-process)