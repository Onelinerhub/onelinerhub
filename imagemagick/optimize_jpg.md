# Optimize JPG images

```bash
convert -strip -interlace Plane -gaussian-blur 0.05 -quality 85% in.jpg out.jpg
```

- -strip - remove any EXIF data
- -interlace Plane - create [progressive JPG](https://medium.com/hd-pro/jpeg-formats-progressive-vs-baseline-73b3938c2339)
- -gaussian-blur 0.05 - bit of blur to reduce image size
- -quality 85% - good quality for most cases
- in.jpg - JPG image that needs to be optimized
- out.jpg - resulting optimized JPG
