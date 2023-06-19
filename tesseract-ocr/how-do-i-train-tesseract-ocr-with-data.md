# How do I train Tesseract OCR with data?
// plain

1. Tesseract OCR can be trained with data using `tesseract_train` command.
2. This command requires two files: a box file and a tif file.
3. The box file contains a list of coordinates of each character in the image and the text associated with it.
4. The tif file is the image that will be used for training.
5. To train Tesseract OCR with data, the following command can be used:
```
tesseract_train --traineddata <output_folder> <box_file> <tif_file>
```
6. This command will create a traineddata file in the specified output folder.
7. To learn more about Tesseract OCR training, please refer to the [Tesseract OCR documentation](https://github.com/tesseract-ocr/tesseract/wiki/Training-Tesseract).

onelinerhub: [How do I train Tesseract OCR with data?](https://onelinerhub.com/tesseract-ocr/how-do-i-train-tesseract-ocr-with-data)