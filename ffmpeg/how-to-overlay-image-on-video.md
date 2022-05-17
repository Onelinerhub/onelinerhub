# How to overlay image on video

```bash
ffmpeg -i in.mp4 -i in.png -filter_complex "[0:v][1:v] overlay=100:100" -pix_fmt yuv420p -c:a copy out.mp4
```

- `-i in.mp4` - input video file
- `-i in.png` - path to image to overlay over a video
- `-filter_complex` - applies specified video/audio complex filter
- `overlay=` - overlays one stream on top of another
- `100:100` - X,Y coordinates to position image (from top left corner)
- `-pix_fmt yuv420p` - use yuv420p pixel format
- `-c:a copy` - copy audio without converting
- `out.mp4` - resulting video file

group: overlay


