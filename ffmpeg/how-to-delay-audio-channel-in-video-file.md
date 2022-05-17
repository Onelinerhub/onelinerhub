# How to delay audio channel in video file 

```bash
ffmpeg -i in.mp4 -itsoffset 5 -i in.mp4 -map 1:v -map 0:a -c copy out.mp4
```

- `-itsoffset` - delays input stream by specified number of seconds
- `5` - delay first input stream (audio channel) by 5 seconds, use negative value to trim instead of delay
- `-i in.mp4` - input video file (first - for audio, and second - for video)
- `-map` - map input channels to output
- `1:v` - use second input (index `1`) for video
- `0:a` - use first input (index `0`) for audio
- `-c copy` - do not encode/convert, only copy
- `out.mp4` - resulting video file

group: itsoffset


