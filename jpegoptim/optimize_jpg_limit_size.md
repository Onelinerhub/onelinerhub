# Optimize JPG image to fit to certain file size

```sql
jpegoptim --strip-all -S 100k img.jpg
```

- jpegoptim - tool to optimize JPG images (```apt install jpegoptim```)
- --strip-all - removes all meta data from file
- -S 100k - try to optimize so that final file size is less than ```100k```
- img.jpg - input image to be optimized (will be overwritten)
