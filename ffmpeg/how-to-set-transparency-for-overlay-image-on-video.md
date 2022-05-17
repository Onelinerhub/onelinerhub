# How to set transparency for overlay image on video

```bash
ffmpeg -i in.mp4 -i in.png -filter_complex "[1]format=yuva444p,colorchannelmixer=aa=0.5[in2];[0][in2]overlay" out.mp4
```

- `-i in.mp4` - input video file
- `-i in.png` - path to image to overlay over a video
- `-filter_complex` - applies specified video/audio complex filter
- `aa=0.5` - sets opacity to 50% for second stream (overlay image)
- `out.mp4` - resulting video file


