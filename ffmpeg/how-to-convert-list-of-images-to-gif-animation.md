# How to convert list of images to GIF animation

```bash
ffmpeg -f image2 -framerate 10 -i in%03d.png out.gif
```

- `-f image2` - special format to operate lists of images
- `-framerate 10` - use 10 images per second (frame rate of 10)
- `-i in%03d.png` - input images template (e.g. `in001.png, in002.png`...)
- `out.gif` - resulting `GIF` animation file

group: gif


