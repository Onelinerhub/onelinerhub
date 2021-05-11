# Resize animated GIF

```bash
convert in.gif -coalesce tmp.gif && convert -size 500x500 tmp.gif -resize 50x50 out.gif
```

- in.gif - input animated GIF
- -coalesce tmp.gif - prepares animation for resize by creating temporary ```tmp.gif``` file, that can be removed after resizing
- -size 500x500 - original GIF file size
- -resize 50x50 - width/height to resize animation to
- out.gif - resized animated GIF
