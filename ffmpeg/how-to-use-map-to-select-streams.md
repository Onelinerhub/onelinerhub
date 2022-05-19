# How to use map to select streams

### If you want to select specific input streams (e.g. first video channel from first file and third audio channel from second file) and use them for your output, you use `map`:

```bash
ffmpeg -i in.mp4 -i in.mp3 -map 0:v:0 -map 1:a:2 out.mp4
```

- `-i in.mp4` - first input (video file)
- `-i in.mp3` - second input (audio file)
- `-map` - maps selected input streams to output
- `0:v:0` - map first video stream of first input
- `1:a:2` - maps third audio stream of second input
- `out.mp4` - resulting video file


