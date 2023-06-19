# How can I use Tesseract OCR with Xamarin Forms?
// plain

Tesseract OCR can be used with Xamarin Forms to enable text recognition from images. The following example code shows how to use Tesseract OCR in a Xamarin Forms project.

```
//Add Tesseract NuGet package to the project
Install-Package Tesseract

//Create a new instance of the TesseractEngine
var engine = new TesseractEngine(@"./tessdata", "eng", EngineMode.Default);

//Load image
var image = new Bitmap(@"./image.png");

//Run OCR on the image
var page = engine.Process(image);

//Get the recognized text
var recognizedText = page.GetText();

//Display the recognized text
Console.WriteLine(recognizedText);
```

## Output example

```
This is a sample text.
```

## Code explanation


1. `Install-Package Tesseract` - This command adds the Tesseract NuGet package to the project.
2. `var engine = new TesseractEngine(@"./tessdata", "eng", EngineMode.Default);` - This line creates a new instance of the TesseractEngine.
3. `var image = new Bitmap(@"./image.png");` - This line loads the image from the specified path.
4. `var page = engine.Process(image);` - This line runs OCR on the image.
5. `var recognizedText = page.GetText();` - This line gets the recognized text from the image.
6. `Console.WriteLine(recognizedText);` - This line displays the recognized text.

## Helpful links

1. [Tesseract OCR for Xamarin](https://github.com/tesseract-ocr/tesseract/wiki/Xamarin)
2. [Tesseract OCR NuGet Package](https://www.nuget.org/packages/Tesseract/)

onelinerhub: [How can I use Tesseract OCR with Xamarin Forms?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-with-xamarin-forms)