# How to resize overlay image on video

```bash
ffmpeg -i in.mp4 -i in.png -filter_complex "[1]scale=50:50,format=yuva444p[in2];[0][in2]overlay" out.mp4
```

- `-i in.mp4` - input video file
- `-i in.png` - path to image to overlay over a video
- `-filter_complex` - applies specified video/audio complex filter
- `scale=50:50` - will resize overlay image by `50x50`
- `out.mp4` - resulting video file

group: overlay


