# How to use presets

```bash
ffmpeg -i in.mp4 -c:v libx264 -preset slow -crf 22 -c:a copy out.mkv
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-c:v libx264` - use H.264 codec
- `-preset` - specify [preset](https://trac.ffmpeg.org/wiki/Encode/H.264#Preset) (mode) to use for conversion, where `ultrafast` is fastest but primitive and `veryslow` is slowest but most efficient
- `slow` - we want to use `slow` preset - average efficiency and speed
- `out.mkv` - resulting file


