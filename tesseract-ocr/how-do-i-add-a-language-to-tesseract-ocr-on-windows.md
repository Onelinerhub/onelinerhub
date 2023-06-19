# How do I add a language to Tesseract OCR on Windows?
// plain

1. Download the language data files you want to add from the [Tesseract language data repository](https://github.com/tesseract-ocr/tessdata).
2. Extract the downloaded language data files to the `tessdata` folder in the Tesseract installation directory.
3. To check if the language data is correctly installed, run the following command in a command prompt, replacing `<lang>` with the language code of the language you installed.

```
tesseract --list-langs
```

The output should include the language code you installed:

```
List of available languages (3):
eng
<lang>
osd
```

4. You can now use the language code to set Tesseract's language when running it from the command line. For example:

```
tesseract image.png output -l <lang>
```

5. If you want to use the language in your own code, you can use the `SetVariable` method of the `TesseractEngine` class. For example:

```csharp
TesseractEngine engine = new TesseractEngine(@"./tessdata", "<lang>");
```

6. You can also set the language when calling the `Process` method of the `TesseractEngine` class. For example:

```csharp
Page page = engine.Process(pix, "<lang>");
```

7. You can find more information about using Tesseract in the [Tesseract.NET documentation](https://tesseract.codeplex.com/documentation).

onelinerhub: [How do I add a language to Tesseract OCR on Windows?](https://onelinerhub.com/tesseract-ocr/how-do-i-add-a-language-to-tesseract-ocr-on-windows)