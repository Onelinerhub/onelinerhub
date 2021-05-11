# Remove EXIF data from image

```bash
identify -format "%wx%h" in.png
```

- in.png - input image
- -format - sets required format for output data
- %wx%h - will return data in ```width x height``` format (e.g. ```125x45```)
