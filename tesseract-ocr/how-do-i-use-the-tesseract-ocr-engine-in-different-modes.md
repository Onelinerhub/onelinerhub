# How do I use the Tesseract OCR engine in different modes?
// plain

The Tesseract OCR engine can be used in three different modes:

1. Command Line Mode: This mode allows users to run Tesseract from the command prompt. An example command to run Tesseract is `tesseract input.jpg output`. This command will take the image file `input.jpg` and create a text file `output.txt` containing the OCR result.

2. C++ API Mode: This mode allows users to call Tesseract from their own C++ programs. An example of this is shown below:
```
#include <tesseract/baseapi.h>

tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();
api->Init(NULL, "eng");
api->SetImage(imagedata);
api->Recognize(0);

tesseract::ResultIterator* ri = api->GetIterator();
if (ri != 0) {
    do {
        const char* word = ri->GetUTF8Text(tesseract::RIL_WORD);
        float conf = ri->Confidence(tesseract::RIL_WORD);
        printf("word: '%s';  \tconf: %.2f\n", word, conf);
        delete[] word;
    } while (ri->Next(tesseract::RIL_WORD));
}

api->End();
```
The code above will take an image as input, run Tesseract on it, and output each word found along with its confidence score.

3. Python API Mode: This mode allows users to call Tesseract from their own Python programs. An example of this is shown below:
```
import tesseract

api = tesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetImage(imagedata)
text=api.GetUTF8Text()
conf=api.MeanTextConf()

print("Text: " + text)
print("Confidence: " + str(conf))
```
The code above will take an image as input, run Tesseract on it, and output the text found along with its confidence score.

## Helpful links

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Tesseract C++ API](https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#c-api)
- [Tesseract Python API](https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#python-api)

onelinerhub: [How do I use the Tesseract OCR engine in different modes?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-the-tesseract-ocr-engine-in-different-modes)