# Resize images in folder and save result to other folder

```bash
mogrify -path /where/to/save/ -resize 200x150 -quality 80 /path/to/images/*.jpg
```

- -path /where/to/save/ - folder to save resulting images to (must exist before you call the command)
- -resize 200x150 - all images will be resized to fit in 200x150 rectangle
- -quality 80 - good quality (increase up to ```100``` for better quality)
- /path/to/images/*.jpg - chooses what files to resize
