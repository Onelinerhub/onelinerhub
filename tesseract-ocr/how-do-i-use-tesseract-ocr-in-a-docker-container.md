# How do I use Tesseract OCR in a Docker container?
// plain

Using Tesseract OCR in a Docker container is a great way to quickly set up a Tesseract environment. Here's how to do it:

1. Pull the official Tesseract OCR Docker image from Docker Hub:

```
docker pull tesseractshadow/tesseract4re
```

2. Create a new Docker container from the image:

```
docker run -it --name tesseract-container tesseractshadow/tesseract4re
```

3. Copy the image you want to OCR into the container:

```
docker cp my_image.jpg tesseract-container:/
```

4. Use the tesseract command to OCR the image:

```
docker exec tesseract-container tesseract my_image.jpg output
```

5. The output will be written to a text file named `output.txt` in the current directory.

6. To retrieve the output file from the container, use the docker cp command:

```
docker cp tesseract-container:/output.txt .
```

7. You can now read the contents of the output file.

## Helpful links
- [Tesseract OCR Docker Hub page](https://hub.docker.com/r/tesseractshadow/tesseract4re)
- [Tesseract OCR GitHub page](https://github.com/tesseract-shadow/tesseract)

onelinerhub: [How do I use Tesseract OCR in a Docker container?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-in-a-docker-container)