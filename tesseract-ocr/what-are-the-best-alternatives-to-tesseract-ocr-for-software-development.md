# What are the best alternatives to Tesseract OCR for software development?
// plain

The best alternatives to Tesseract OCR for software development are:

1. **Google Cloud Vision**: This is an API for recognizing text, objects, and faces in images. It supports a wide range of languages and provides accurate results. Example code:

```
from google.cloud import vision

client = vision.ImageAnnotatorClient()

image = vision.types.Image()
image.source.image_uri = 'gs://cloud-samples-data/vision/text/screen.jpg'

response = client.text_detection(image=image)

print(response.text_annotations[0].description)
```
## Output example

```
Google Cloud Platform
```

2. **Microsoft Computer Vision API**: This is an API for recognizing text, objects, and faces in images. It supports a wide range of languages and provides accurate results. Example code:

```
import requests

subscription_key = '<subscription_key>'

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

ocr_url = vision_base_url + "ocr"

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params  = {'language': 'unk', 'detectOrientation': 'true'}

data    = {'url': image_url}

response = requests.post(ocr_url, headers=headers, params=params, json=data)

response.raise_for_status()

analysis = response.json()

print(analysis)
```

## Output example

```
{'language': 'en',
 'textAngle': 0.0,
 'orientation': 'Up',
 'regions': [{'boundingBox': '21,20,295,51',
   'lines': [{'boundingBox': '21,20,295,51',
     'words': [{'boundingBox': '21,20,295,51',
       'text': 'Nothing'},
      {'boundingBox': '128,20,187,51', 'text': 'exists'}]}]}]}
```

3. **Amazon Rekognition**: This is an API for recognizing text, objects, and faces in images. It supports a wide range of languages and provides accurate results. Example code:

```
import boto3

client=boto3.client('rekognition')

response = client.detect_text(Image={'S3Object':{'Bucket':'mybucket','Name':'text.jpg'}})

textDetections=response['TextDetections']

print (textDetections)
```

## Output example

```
[{'DetectedText': 'Hello World!',
  'Type': 'LINE',
  'Id': 0,
  'Confidence': 99.9886474609375,
  'Geometry': {'BoundingBox': {'Width': 0.07907845195051193,
    'Height': 0.037991712391376496,
    'Left': 0.4650304317474365,
    'Top': 0.4545999765396118},
   'Polygon': [{'X': 0.4650304317474365, 'Y': 0.4545999765396118},
    {'X': 0.5440995812416077, 'Y': 0.4545999765396118},
    {'X': 0.5440995812416077, 'Y': 0.4925917148590088},
    {'X': 0.4650304317474365, 'Y': 0.4925917148590088}]}}]
```

4. **Kairos OCR**: This is an API for recognizing text, objects, and faces in images. It supports a wide range of languages and provides accurate results. Example code:

```
import requests

url = 'https://api.kairos.com/recognize'

headers = {
    'app_id': '<app_id>',
    'app_key': '<app_key>'
}

data = {
    'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png'
}

response = requests.post(url, headers=headers, json=data)

print(response.json())
```

## Output example

```
{'status': 'Complete',
 'images': [{'transaction': {'status': 'success',
    'subject_id': None,
    'gallery_name': None,
    'confidence': 0.937,
    'width': 338,
    'height': 338,
    'topLeftX': 0,
    'topLeftY': 0,
    'timestamp': '1566981466.86',
    'quality': 0.851,
    'eyeDistance': 0.0},
   'candidates': [{'subject_id': 'Nothing exists',
     'confidence': 0.937,
     'enrollment_timestamp': '1566981466.86'}]}]}
```

## Helpful links
- [Google Cloud Vision](https://cloud.google.com/vision/)
- [Microsoft Computer Vision API](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)
- [Amazon Rekognition](https://aws.amazon.com/rekognition/)
- [Kairos OCR](https://www.kairos.com/docs/api/)

onelinerhub: [What are the best alternatives to Tesseract OCR for software development?](https://onelinerhub.com/tesseract-ocr/what-are-the-best-alternatives-to-tesseract-ocr-for-software-development)