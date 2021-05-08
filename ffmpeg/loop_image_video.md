# Create video file from a single image (loop image in video)

```bash
ffmpeg -loop 1 -i im.png -c:v libx264 -t 30 -pix_fmt yuv420p -vf scale=1920:1080 out.mp4
```

- im.png - image file to create video from
- -c:v libx264 - uses h264 codec
- -t 30 - creates a 30 seconds video (or specify any other length in seconds)
- -pix_fmt yuv420p - color saving format (just leave it as is)
- scale=1920:1080 - resulting video resolution
- out.mp4 - resulting video file
