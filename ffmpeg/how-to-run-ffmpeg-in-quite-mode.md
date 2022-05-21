# How to run ffmpeg in quite mode

```bash
ffmpeg -hide_banner -loglevel error -i in.mp4 out.mp4
```

- `-hide_banner` - skip version details
- `-loglevel error` - set logging level to errors only
- `-i in.mp4` - input video file
- `out.mp4` - resulting video file

group: verbosity


link_youtube: https://youtu.be/M7yhFVJ4fq0
