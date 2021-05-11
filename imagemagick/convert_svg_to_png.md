# How to convert SVG to PNG

```bash
convert -density 2000x2000 -resize 1000x1000 image.svg image.png
```

- -density 2000x2000 - sets resolution for good quality
- -resize 1000x1000 - what width/height you need for your PNG?
- image.svg - input SVG file
- image.png - resulting PNG image


alternative_tech: inkscape

```bash
inkscape -z -w 1000 -h 1000 image.svg -e image.png
```

- -z - enables command line mode
- -w 1000 - what width you need for your PNG
- -h 1000 - what height you need for your PNG
- image.svg - input SVG file
- image.png - resulting PNG image
