# How do I use tesseract OCR to create bounding boxes?
// plain

Tesseract OCR is an open source optical character recognition (OCR) engine. It can be used to create bounding boxes around text in images.

To use Tesseract OCR to create bounding boxes, you need to first install the Tesseract library. For example, on Ubuntu you can use the following command:
```
sudo apt-get install tesseract-ocr
```

Once the library is installed, you can use the following Python code to create bounding boxes around text in an image:
```
from PIL import Image
import pytesseract
import cv2

# Load the image
image = cv2.imread('example.jpg')

# Create a copy of the image
img_copy = image.copy()

# Use Tesseract to detect text in the image
text = pytesseract.image_to_data(image)

# Create a list of bounding boxes
bboxes = []
for x, bbox in enumerate(text.splitlines()):
	if x != 0:
		bbox = bbox.split()
		if len(bbox) == 12:
			x, y, w, h = int(bbox[6]), int(bbox[7]), int(bbox[8]), int(bbox[9])
			bboxes.append((x, y, w, h))

# Draw the bounding boxes on the image
for bbox in bboxes:
	x, y, w, h = bbox
	cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 0, 255), 1)

# Show the image
cv2.imshow('Image with Bounding Boxes', img_copy)
cv2.waitKey(0)
```

This code will produce an image with bounding boxes around the detected text, as shown in the following image:

![Bounding Boxes](example_bbox.jpg)

The code works by first loading the image, then using Tesseract to detect text in the image. Once the text is detected, the code creates a list of bounding boxes around the text. Finally, the code draws the bounding boxes on the image and displays it.

## Helpful links

- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract/wiki)
- [pytesseract Documentation](https://pypi.org/project/pytesseract/)
- [OpenCV Documentation](https://opencv.org/documentation/)

onelinerhub: [How do I use tesseract OCR to create bounding boxes?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-to-create-bounding-boxes)