# How do I add Tesseract OCR to my environment variables?
// plain

Adding Tesseract OCR to your environment variables is a simple process.

First, you need to find the directory of your Tesseract OCR installation. This can usually be found by searching for the Tesseract executable file.

Once you have the directory, you can add it to your environment variables with the following command:
```
setx PATH "%PATH%;<path_to_your_tesseract_directory>"
```
For example, if your Tesseract directory is located at `C:\Program Files\Tesseract-OCR`, you can add it to your environment variables with the following command:
```
setx PATH "%PATH%;C:\Program Files\Tesseract-OCR"
```
The output of this command should be `SUCCESS: Specified value was saved.`.

You can also use the `set` command instead of `setx` to set environment variables for the current session only.

For more information about environment variables, please refer to the [Microsoft Documentation](https://docs.microsoft.com/en-us/windows/win32/procthread/environment-variables).

onelinerhub: [How do I add Tesseract OCR to my environment variables?](https://onelinerhub.com/tesseract-ocr/how-do-i-add-tesseract-ocr-to-my-environment-variables)