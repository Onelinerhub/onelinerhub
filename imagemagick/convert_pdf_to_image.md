# Convert PDF to image

```bash
convert -density 300 -trim in.pdf -quality 100 -flatten out.jpg
```

- -density 300 - sets good image resolution
- -trim - will optimize resulting image by removing unnecessary data
- in.pdf - PDF file to convert to image
- -quality 100 - best possible quality
- -flatten - will reduce resulting image file size
- out.jpg - resulting image
