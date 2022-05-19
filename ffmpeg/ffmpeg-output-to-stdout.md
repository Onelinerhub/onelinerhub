# ffmpeg output to stdout

```bash
ffmpeg -i in.mp4 -f avi pipe:1
```

- `-i in.mp4` - input video file
- `-f avi` - we need to specify output format since we use piping
- `pipe:1` - send output to `stdout` instead of file


link_youtube: https://youtu.be/vBvsOvQD2dI
