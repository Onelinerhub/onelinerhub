# How to crop video

```bash
ffmpeg -i in.mp4 -vf "crop=iw/2:ih/2" out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `crop=` - crop video
- `iw/2:ih/2` - half of original video size and height, centered
- `out.mp4` - resulting video file

group: zoom


link_youtube: https://youtu.be/7GJ89cWT11Q
